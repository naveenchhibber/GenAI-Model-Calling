# need OpenAI Key >> Go to platform.openai.com  >> Create Account >> You need some credit >> recharge
# To intigrate OpenAI and Langchain import package
# OpenAI is a base model of OpenAI for LLM 
from langchain_openai import OpenAI
# Load seceret keys from .env file to here 
from dotenv import load_dotenv
# initialize .env file to get secret keys
load_dotenv()

# Create a object of OpenAI and mention model you want to use 
# LLM Models can take input as string and give output in string format only.
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# call invoke function from llm object to communicate with gpt model, here we will send our query.
# output of invoke function will be saved in result variable.
result = llm.invoke("What is the capital of India")

print(result)

# go to terminal and run as [(venv) PS K:\GenAI-Model-Calling> python .\2-InvokingLLM.py]


