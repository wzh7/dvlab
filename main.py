# ==== ============ ==== #
# ====     Main     ==== #
# ==== ============ ==== #

import sys
sys.path.append("util")
import time
import threading
import ai
import log
import echarts_test as et
import gradio_test as gr

event = threading.Event()

# Global variables
global gpt_reply

class FlaskThread(threading.Thread):
    '''Flask网页线程'''
    def run(self) -> None:
        log.info("线程管理", "线程-Flask网页 开始运行")
        et.run_flask() # 运行Flask网页
        
class AIThread(threading.Thread):
    '''AI线程'''
    def run(self) -> None:
        log.info("线程管理", "线程-ChatGPT网页 开始运行")
        gr.run_gradio() # 运行ChatGPT网页

# class SpeakThread(threading.Thread):
#     '''语音线程'''
#     def run(self) -> None:
#         log.info("线程管理", "线程-语音 开始运行")
#         tts.speak(gpt_reply) # 语音合成
#         event.set() # 语音合成完成，设置event

if __name__ == '__main__':
    log.info("系统", "欢迎使用ChatEase，正在启动程序...")
    t = FlaskThread()
    b = AIThread()
    t.start()
    b.start()