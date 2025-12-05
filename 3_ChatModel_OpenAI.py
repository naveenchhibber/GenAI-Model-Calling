# Import Chat Model from OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Make object of ChatOpenAI 
# temperature value from 0 - 2, to control how much creative response you want, higher the value the result would be more random and creative. 
# max_completion_tokens how many tokens you want in output
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("Write a 5 line poem on cricket")

# Only content without metadata
print(result.content)

# Complete result with metadata
print(result)
