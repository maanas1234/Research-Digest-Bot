from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    return ChatOpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENAI_API_KEY"), model="qwen/qwen3.6-plus:free"   # you can change model here
)



