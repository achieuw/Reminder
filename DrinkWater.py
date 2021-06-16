import time
from plyer import notification

def ReminderWater(title, message) :
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Reminder\\water_glass.ico",
        timeout = 10,
    )

def ReminderBreak(title, message, timeout) :
    notification.notify(
        title = title, 
        message = message,
        app_icon = None,
        timeout = timeout,

    )

counter = 1
break_timeout = 20
if __name__ == "__main__":
    while True : 
        ReminderBreak("Break time", "Look at something atleast 6 meters away for 20 seconds", break_timeout)
        counter += 1
        time.sleep(break_timeout + 1) # Sleep for notification timeout duration

        if(counter == 2) :
            ReminderWater("Drink water", "Time to take a sip!")
            counter = 0

        time.sleep(60*20)