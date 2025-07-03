import time
import platform
import schedule
from datetime import datetime
from plyer import notification

def remind_to_drink():
    current_hour = datetime.now().hour
    # Sleep mode from 10 PM (22) to 7 AM (7)
    if current_hour >= 22 or current_hour < 7:
        print(" Night-time mode: No reminders right now.")
        return

    notification.notify(
        title=" Water Reminder",
        message="Time to drink water! Stay hydrated ",
        timeout=10
    )

    # Optional beep (Windows only)
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 500)
        except ImportError:
            pass

# Schedule every hour
schedule.every(1).hours.do(remind_to_drink)

print("Water Reminder with Sleep Mode started... Press Ctrl+C to stop.")

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)
