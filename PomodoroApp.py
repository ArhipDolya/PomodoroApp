import time
from tkinter import *



def start_timer():
    total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())

    while total_seconds > 0:
        hours.set(str(total_seconds // 3600).zfill(2))
        minutes.set(str((total_seconds % 3600) // 60).zfill(2))
        seconds.set(str(total_seconds % 60).zfill(2))
        window.update()
        time.sleep(1)
        total_seconds -= 1


window = Tk()
window.title("PomodoroApp")

window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

WIDTH = 650
HEIGHT = 350

X = (window_width//2) - (WIDTH//2)
Y = (window_height//2) - (HEIGHT//2)

window.configure(background='red')
window.geometry(f'{WIDTH}x{HEIGHT}+{X}+{Y}')


hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set('00')
minutes.set('00')
seconds.set('00')

X_INPUTS = 200
Y_INPUTS = 40

hoursInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=hours)
hoursInput.place(x=X_INPUTS, y=Y_INPUTS)

minutesInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=minutes)
minutesInput.place(x=X_INPUTS + 100, y=Y_INPUTS)

secondsInput = Entry(window, width=3, font=('Arial', 20, ''), textvariable=seconds)
secondsInput.place(x=X_INPUTS + 200, y=Y_INPUTS)

start_button = Button(window, text='Start Pomodoro', font=('Arial', 18, 'bold'), command=start_timer)
start_button.place(x=220, y=220)


if __name__ == '__main__':
    window.mainloop()