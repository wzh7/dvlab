import requests
import openai # AI库
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
) # 请求重试库
import wzh.log as log

# AI库的API Key
openai.api_key = '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'
# 提示词
prompt = "请不要有额外的回复内容，我给你数据，请用{'value':1000, 'name': '名字'}的格式回复我"
# prompt = "你好"

# 指数增长重试时间1秒到60秒，最大重试次数为6次
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def gpt(content:str):
    '''GPT用户对话'''
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                messages=[
                                    {"role":"user","content":content},
                                    {"role":"system","content":prompt}])
    log.info("GPT", response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']

def gpt_talk(content:str):
    try:
        reply = gpt(content)
        return reply
    except Exception as e:
        log.error("GPT", e)

def run_chat():
    while(True):
        content = input("\033[93m[用户]\033[0m 输入 ：")
        gpt_talk(content)

if __name__ == '''__main__''':
    run_chat()