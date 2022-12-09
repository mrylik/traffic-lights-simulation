from tkinter import *


class Timer:
    def __init__(self):
        self.running = False
        self.seconds = 0
        self.minutes = 0
        self.timer_label = Label(text='00:00', font=('Roboto', 40))
        self.update_timer = ''

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False
        self.timer_label.after_cancel(self.update_timer)

    def update(self):
        if self.running:
            self.seconds += 1

            if self.seconds == 59:
                self.minutes += 1
                self.seconds = 0

        seconds = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        minutes = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'

        self.timer_label.config(text=f'{minutes}:{seconds}',
                                font=('Roboto', 40))
        self.update_timer = self.timer_label.after(1000, self.update)

