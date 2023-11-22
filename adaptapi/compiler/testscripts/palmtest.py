import pprint
import google.generativeai as palm
from dotenv import load_dotenv
import os


load_dotenv()
palm.configure(api_key=os.getenv("PALM_API_KEY"))

prompt = """
return the correct result for this AST: ('program', ('statements', ('statement', ('whileloop', ('assignment', 'i', ('value', 0)), ('condition', ('identifier', {'datatype': 'int', 'value': ('value', 0)}), '<', ('value', 10)), ('statements', ('statements', ('print', ('identifier', {'datatype': 'int', 'value': ('value', 0)})), 'statement', ('decrement', '++')))))))"""

prompt2 = """return the correct result for this AST:
('program', ('statements', ('statements', ('statements', ('statements', ('statements', ('assignment', 'a', ('value', 2)), 'assignment', 'b', ('value', 3)), 'statement', ('function-impl', 'sum', 'int', ('statements', ('return', ('binop', ('identifier', {'datatype': 'int', 'value': ('value', 2)}), '+', ('identifier', {'datatype': 'int', 'value': ('value', 3)})))))), 'assignment', 'total', None), 'print', ('identifier', {'datatype': 'int', 'value': None}))))

"""

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

completion = palm.generate_text(
    model=model,
    prompt=prompt2,
    temperature=0,
    max_output_tokens=800,
)
pprint.pprint(completion.result)