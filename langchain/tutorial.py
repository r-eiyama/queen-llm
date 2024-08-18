from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import config
import os

os.environ["AZURE_OPENAI_API_KEY"] = config.AZURE_OPENAI_API_KEY
os.environ["AZURE_OPENAI_ENDPOINT"] = config.AZURE_OPENAI_ENDPOINT
os.environ["AZURE_OPENAI_API_VERSION"] = "2023-05-15"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gpt-4o"


model = AzureChatOpenAI(
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

messages = [
    SystemMessage(content="あなたは日本人のピカチュウです。日本語でピカチュウになりきって応答してください"),
    HumanMessage(content="こんにちは！カメックスです"),
]

res = model.invoke(messages)

print(res.content)

