# jump.PY
import time

def start_timer(duration):
    while duration >= 0:
        minutes, seconds = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end='\r')
        time.sleep(1)
        duration -= 1
    print("Таймер завершен!")

duration = 300  # 5 минут
start_timer(duration)
