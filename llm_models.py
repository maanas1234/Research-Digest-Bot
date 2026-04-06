from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def get_llm_offline():
    return ChatOpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENROUTER_API_KEY"), model="openai/gpt-oss-120b:free"   # you can change model here
)
def get_llm_online():
    return ChatOpenAI(base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENROUTER_API_KEY"), model="qwen/qwen3.6-plus:free:online"   # you can change model here
)






