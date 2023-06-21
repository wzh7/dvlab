import gradio as gr
import wzh.ai as ai
# import cv2

# def to_black(image):
#     output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     return output

# interface = gr.Interface(fn=to_black, inputs="image", outputs="image")
# interface.launch()

def ChatGPT_Bot(input):
    if input:
        reply = ai.gpt_talk(input)
        return reply

def run_gradio():
    '''运行gradio'''
    inputs = gr.Textbox(lines=7, label="请输入你的问题")
    outputs = gr.Textbox(lines=7, label="来自ChatGPT的回答")

    gr.Interface(fn=ChatGPT_Bot, inputs=inputs, outputs=outputs, title="ChatGPT AI助理",
                description="我是您的AI助理，您可以问任何你想知道的问题",
                theme=gr.themes.Default()).launch(share=True)