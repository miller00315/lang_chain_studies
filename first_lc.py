from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print(demosimple.__doc__)

    demosimple()

def demosimple():
    """
    This function demostrates a simple of LCEL (Langchain Expression Langauge) to create a custom Chain with the Prompt and Model
    """

    # Create the Prompt template
    prompt = ChatPromptTemplate.from_template("Tell me a few achievements of {name}")

    # Create the LLM Object (options between OpenAI GPT or Gemini)
    model = ChatOpenAI(
        model_name="gpt-3.5-turbo", 
        openai_api_key=os.getenv('GOOGLE_API_KEY'), 
        temperature=0.5
    )

    # Create the chain
    chain = prompt | model # LCEL - LangChain Expresion Language

    # Invoke (run) the Chain - The Chat Model returns a Message
    print(chain.invoke({"name": "Barack Obama"}).content)

if __name__ == "__main__":
    main()


