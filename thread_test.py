import time
import threading

event = threading.Event()
event.set()     # 设定Flag = True

class WzhThread(threading.Thread):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def run(self) -> None:
        if self.n in [3, 4]:
            event.clear()   # 设定Flag = False
            event.wait()    # 线程3和4进入等待
        
        for i in range(2):
            _count = threading.active_count() - 1
            print(f"线程-{self.n}", f"当前活跃的子线程个数：{_count}")
            time.sleep(2)
            if self.n == 2 and i == 1:
                # 通过线程2来控制线程3和4
                event.set()

for i in range(1, 5):
    t = WzhThread(i)
    t.start()