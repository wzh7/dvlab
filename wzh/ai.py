import requests
import openai # AI库
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
) # 请求重试库

# AI库的API Key
openai.api_key = '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'
# 提示词
prompt = "请不要有额外的回复内容，我给你数据，请用{'value':1000, 'name': '名字'}的格式回复我"
print("\033[93m[GPT]\033[0m提示词：" + prompt)

# 指数增长重试时间1秒到60秒，最大重试次数为6次
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def gpt(content:str):
    '''GPT用户对话'''
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                messages=[
                                    {"role":"user","content":content},
                                    {"role":"system","content":prompt}])
    print("\033[93m[GPT]\033[0m回复：" + response['choices'][0]['message']['content'])

def gen_mbti():
    gpt("")


if __name__ == '''__main__''':
    while(True):
        content = input("\033[93m[GPT]\033[0m输入：")
        gpt(content)