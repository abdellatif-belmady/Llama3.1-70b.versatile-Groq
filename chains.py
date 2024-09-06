import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class MoroccanCuisineGenerator:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def generate_recipe(self, dish_name, dietary_restrictions=None):
        prompt_template = PromptTemplate.from_template(
            """
            Generate an authentic Moroccan recipe for {dish_name}. 
            Dietary restrictions to consider: {dietary_restrictions}.
            
            Provide the following information in JSON format:
            1. Ingredients (with measurements)
            2. Cooking instructions (step-by-step)
            3. Cooking time and difficulty level
            4. Cultural significance and history of the dish
            5. Serving suggestions and traditional accompaniments
            
            Ensure all text is in both English and Arabic.
            
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain = prompt_template | self.llm | JsonOutputParser()
        try:
            result = chain.invoke({"dish_name": dish_name, "dietary_restrictions": dietary_restrictions})
            return result
        except OutputParserException:
            raise OutputParserException("Unable to generate a valid recipe.")

    def get_cultural_insights(self, ingredient_or_technique):
        prompt_template = PromptTemplate.from_template(
            """
            Provide detailed cultural insights about the Moroccan {subject}, including:
            1. Historical background
            2. Traditional uses in Moroccan cuisine
            3. Regional variations within Morocco
            4. Any symbolic or cultural significance
            5. Modern adaptations or uses
            
            Provide the information in both English and Arabic.
            
            ### INSIGHTS (NO PREAMBLE):
            """
        )
        chain = prompt_template | self.llm
        result = chain.invoke({"subject": ingredient_or_technique})
        return result.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))