import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import ast
from datetime import datetime
load_dotenv()

class Chain:
    def __init__(self):
        self.llm=ChatGroq(
        temperature=0,
        groq_api_key=os.getenv('GROQ'),
        model_name="llama-3.3-70b-versatile"
        )
    def fraud_detection(self,txt):
        ptext=PromptTemplate.from_template("""
        ###Customer reviews of zomato:
        {pagecon}
        Detect if the review is fraudulent or not.
        Fraud reviews will be over-exaggerated.
        Some examples:
            The Lasagna was hearty and rich. Could use more béchamel sauce. - False
            The Spaghetti here is so divine I cried while eating. Pure heaven! - True
            Carbonara was creamy, pancetta well cooked. - False
        Return a boolean value only. True or False (True for Fraud , False for Actual review) Not a function but Value
        ###Valid python boolean . Dont mark all as True No PREAMBLE: 
        """)    
        chext=ptext | self.llm
        r=chext.invoke(input={'pagecon': txt})
        try:
           rnew=ast.literal_eval(r.content)
        except :
            raise Exception("Not a boolean!!!")
        return rnew
    
    def recomm(self,reviews,items):
        prompt_email = PromptTemplate.from_template(
            """
            ### Reviews:
            {rev}
            

            ### INSTRUCTION:
            You are a recommendation system see my reviews. Choose the item from {items} only (even if item is present in review if its not from item list it does not count ) based on:
            which is the most liking and 
            time: {current_time} to check it is time for what: breakfast,lunch,dinner,snacks,sweets,etc. 
            Do not provide a preamble.
            ###return chosen item as a tuple: (name of item from the chosen item,price from the chosen item).DONT RETUN FUNCTION BUT A VALID PYTHON TUPLE. NO PREAMBLE:

            """
        )
        chain_email=prompt_email | self.llm
        rn=chain_email.invoke({"rev":str(reviews),"items":str(items),"current_time":datetime.now().strftime("%H:%M")})
     

        return ast.literal_eval(rn.content)

    def search(self,query,items):
            prompt_email = PromptTemplate.from_template(
                """
                ### Item Description:
                {query}
                

                ### INSTRUCTION:
                You are a search system see my item description. Choose the items from {items} only (if its not from item list it does not count ) based on:
                which are the most suitable items according to the description Provide results that are most related
                NO indirect relation or sub direct relation 
                Do not provide a preamble.
                ###return chosen items as a list of tuples: [(name of item from the chosen item,price from the chosen item), (...),(...), ].max_lenght of list 5,min_lenght 1,arrange them based on how fit they are for query .DONT RETUN FUNCTION BUT A VALID PYTHON TUPLE. NO PREAMBLE:
                 NOT TUPLE OF TUPLES BUT LIST OF TUPLES
                """
            )
            chain_email=prompt_email | self.llm
            rn=chain_email.invoke({"query":str(query),"items":str(items)})
            # print(rn.content)
            return ast.literal_eval(rn.content)