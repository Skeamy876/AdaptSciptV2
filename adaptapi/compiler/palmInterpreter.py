import google.generativeai as palm
from dotenv import load_dotenv
import os


load_dotenv()
class PalmInterpreter:
    def __init__(self):
        palm.configure(api_key=os.getenv("PALM_API_KEY"))
        self.models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        self.model = self.models[0].name

    def interpret(self, ast):
        prompt = f"return the correct result for this AST: {ast}"
        completion = palm.generate_text(
            model=self.model,
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,
        )
        return completion.result