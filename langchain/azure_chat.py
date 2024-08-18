from langchain_openai import AzureChatOpenAI
from langchain.callbacks import get_openai_callback
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

message = "人生とは何か？100文字以内でこの質問に答えてください。"

with get_openai_callback() as cb:
    res = model.invoke([message])
    print(res.content)
    print(
        f"Total Cost (USD): ${format(cb.total_cost, '.6f')}"
    )

