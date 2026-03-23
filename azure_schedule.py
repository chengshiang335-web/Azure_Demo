
from datetime import datetime
import time
import schedule

def sayHello():
    now = datateime.now()

    print("固定等十秒钟，当前时间：", now)


schedule.every(10).seconds.do(sayHello)

while True:
    schedule.run_pending()
    time.sleep(1)   

