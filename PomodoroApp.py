import time
from tkinter import *
from plyer import notification
import pygame

from sound import SOUND



def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def start_timer(should_start=True):
    global TIMER_RUNNING

    if should_start:
        TIMER_RUNNING = True

    total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())

    while total_seconds > 0 and TIMER_RUNNING:
        hours.set(str(total_seconds // 3600).zfill(2))
        minutes.set(str((total_seconds % 3600) // 60).zfill(2))
        seconds.set(str(total_seconds % 60).zfill(2))
        window.update()
        time.sleep(1)
        total_seconds -= 1

    if total_seconds == 0:
        # When the timer is finished, it displays notifications
        notification_title = "Pomodoro Timeer"
        notification_message = "Hi :) Time is up! It's time to take a break!"

        play_alarm_sound()
        notification.notify(title=notification_title, message=notification_message, timeout=5)


def pause_resume_timer():
    global TIMER_RUNNING

    if TIMER_RUNNING:
        TIMER_RUNNING = False
    else:
        TIMER_RUNNING = True
        start_timer()


def reset_timer():
    global TIMER_RUNNING

    TIMER_RUNNING = False
    hours.set('00')
    minutes.set('25')
    seconds.set('00')


window = Tk()
window.title("PomodoroApp")

window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

# Constants

WIDTH = 650
HEIGHT = 350

X = (window_width//2) - (WIDTH//2)
Y = (window_height//2) - (HEIGHT//2)

TIMER_RUNNING = True

X_INPUTS = 200
Y_INPUTS = 40



window.configure(background='red')
window.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')


hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set('00')
minutes.set('25')
seconds.set('00')

# Entries
hoursInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=hours)
hoursInput.place(x=X_INPUTS, y=Y_INPUTS)

minutesInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=minutes)
minutesInput.place(x=X_INPUTS + 100, y=Y_INPUTS)

secondsInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=seconds)
secondsInput.place(x=X_INPUTS + 200, y=Y_INPUTS)


# Buttons
start_button = Button(window, text='Start Pomodoro', font=('Arial', 12, 'bold'), command=start_timer)
start_button.place(x=80, y=210)

pause_button = Button(window, text='Pause/Resume Pomodoro', font=('Arial', 12, 'bold'), command=pause_resume_timer)
pause_button.place(x=225, y=210)

reset_button = Button(window, text='Reset Pomodoro', font=('Arial', 12, 'bold'), command=reset_timer)
reset_button.place(x=450, y=210)



if __name__ == '__main__':
    window.mainloop()