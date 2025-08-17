import time
import datetime
from plyer import notification

def reminder(interval=45, message="💧 Time to drink water!"):
    try:
        while True:
            notification.notify("Hydration Reminder", message)
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Reminder sent")
            time.sleep(interval * 60)
    except KeyboardInterrupt:
        print("\nStopped. Stay hydrated!")

if __name__ == "__main__":
    reminder(interval=45)