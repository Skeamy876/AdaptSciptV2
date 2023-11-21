from  openai import OpenAI
from dotenv import load_dotenv
import os



# API REQUEST ARE LIMITED, DO NOT USE
class GPTInterpreter:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def execute_with_gpt(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a code interpreter for AST list, you will only execute loops and functions"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content