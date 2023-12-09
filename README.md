## AdaptScript Programming Language
# overview
AdaptScript is a general-purpose programming language designed and implemented using PLY (Python Lex-Yacc). This project provides support for essential programming language features, including iteration, control structures, arithmetic operations, functions, and loops. The language is developed with a focus on simplicity, flexibility, and ease of use.

# Features
Lexical and Syntax Analysis: The project includes a well-defined tokenizer and parser to perform lexical and syntax analysis on AdaptScript code.

Arithmetic Operations: AdaptScript supports a wide range of arithmetic operations, allowing users to perform mathematical computations within their programs.

Control Structures: Conditional statements and loops are integral to any programming language, and AdaptScript provides robust support for building structured and efficient control flow in your code.

Functions: Users can define and use functions to encapsulate and reuse code, promoting modular and maintainable programming practices.

Parse Tree Generation: The syntactically and semantically correct input string is converted into a parse tree, which serves as an intermediate representation of the code structure.

Flask API Integration: The project includes a Flask API that enables developers to integrate AdaptScript compilation and execution into their applications.

Integration with PALM2 LLM: The parse tree is then sent to the PALM2 Language Level Machine (LLM) for code interpretation and optimization. This integration allows for efficient execution and improved performance of AdaptScript programs.

# Getting Started
To get started with AdaptScript, follow these steps:

1. Clone the Repository:
```
git clone https://github.com/your-username/AdaptScripV2.git
cd AdaptScripV2
```
2. Install dependencies
```
python -m install -r requirements.txt
```
3. Create a .env file and from here you will place your PALM_API_KEY key. See https://ai.google/discover/palm2 for reference
4. Now you can run either of the scripts included. Happy coding!!

5. For a Flask integration Example see the https://github.com/Skeamy876/AdaptScript_App. Details for set up are included in the documentation for this.


