import requests
import openai
openai.api_key = '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'

def img_test():
    '''创建图片示例'''
    response = openai.Image.create(
        prompt="天安门广场前的AE86",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)


def chatgpt_test():
    '''创建chatGPT示例'''
    # 分三种角色system、assistant、user
    # system的作用是设定助手的行为，可以填入chatgpt-prompts
    # user是最终的用户输入
    # assistant是当chatGPT忘记了上下文，就可以用来存储先前的响应，给chatGPT提供所需的行为实例
    response=openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                messages=[{"role":"user","content":"怎么申请visa信用卡"}])
    print(response['choices'][0]['message']['content'])


if __name__ == '''__main__''':
    chatgpt_test()