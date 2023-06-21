# ==== ============ ==== #
# ====     Main     ==== #
# ==== ============ ==== #

import time
import threading
import wzh.ai as ai
import wzh.log as log
import echarts_test as et
import gradio_test as gr

event = threading.Event()

class FlaskThread(threading.Thread):
    
    def run(self) -> None:
        log.info("线程管理", "线程-Flask网页 开始运行")
        et.run_flask() # 运行Flask网页
        
class AIThread(threading.Thread):
    
    def run(self) -> None:
        log.info("线程管理", "线程-ChatGPT网页 开始运行")
        gr.run_gradio() # 运行ChatGPT网页

if __name__ == '__main__':
    log.info("系统", "欢迎使用ChatEase，正在启动程序...")
    t = FlaskThread()
    b = AIThread()
    t.start()
    b.start()