from openai import AzureOpenAI
import config

# ２　APIクライアントの設定
client = AzureOpenAI(
    api_key = config.AZURE_OPENAI_API_KEY,
    api_version = '2023-05-15', # this might change in the future
    azure_endpoint = config.AZURE_OPENAI_ENDPOINT, # your endpoint should look like the following 
)
# ３　API呼出方法
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "日本で一番高い山を教えて下さい。"},
    ],
)
# ４　レスポンスの処理
print(response.choices[0].message.content)