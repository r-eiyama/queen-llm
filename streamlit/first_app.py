import streamlit as st
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

# https://zenn.dev/ml_bear/books/d1f060a3f166a5/viewer/0e8fe3
def main():

    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    st.header("My Great ChatGPT 🤗")

    if user_input := st.chat_input("聞きたいことを入力してね！"):
        # なにか入力されればここが実行される
        pass

if __name__ == '__main__':
    main()