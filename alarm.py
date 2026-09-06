import datetime
import time

alarm_time = input("Set alarm (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print(" Wake up!")
        break
    time.sleep(10)




