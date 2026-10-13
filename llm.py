from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

_llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


def invoke(prompt: str) -> str:
    response = _llm.invoke(prompt)
    return response.text