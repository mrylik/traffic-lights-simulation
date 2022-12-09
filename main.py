from tkinter import *
from traffic_indicator import TrafficIndicator
from timer import Timer
from juncture import Juncture


def main():
    root = Tk()
    root.geometry('850x850')
    root.title('Traffic Lights')

    bg = PhotoImage(file='background.png')
    
    canvas1 = Canvas(root, width=850, height=850)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    timer = Timer()
    canvas1.create_window(650, 110, window=timer.timer_label)

    timer_start = Button(text='Start', font=('Roboto', 23),
                         command=lambda: [timer.start(),
                                          juncture.traffic_start()])
    timer_stop = Button(text='Stop', font=('Roboto', 24),
                        command=lambda: [timer.stop(), juncture.traffic_stop()])

    canvas1.create_window(780, 80, window=timer_start)
    canvas1.create_window(780, 130, window=timer_stop)

    indicator1 = TrafficIndicator((100, 40, 200, 250),
                                  green_light=(100, 40, 200, 110),
                                  yellow_light=(100, 110, 200, 180),
                                  red_light=(100, 180, 200, 250),
                                  canvas=canvas1)

    indicator2 = TrafficIndicator((0, 610, 270, 690),
                                  red_light=(180, 610, 270, 690),
                                  yellow_light=(90, 610, 180, 690),
                                  green_light=(0, 610, 90, 690),
                                  canvas=canvas1)

    indicator3 = TrafficIndicator((730, 600, 630, 820),
                                  red_light=(730, 600, 630, 675),
                                  yellow_light=(730, 675, 630, 745),
                                  green_light=(730, 745, 630, 820),
                                  canvas=canvas1)

    indicator4 = TrafficIndicator((570, 170, 840, 250),
                                  red_light=(570, 170, 660, 250),
                                  yellow_light=(660, 170, 750, 250),
                                  green_light=(750, 170, 840, 250),
                                  canvas=canvas1)

    juncture = Juncture(indicator1, indicator2, indicator3, indicator4, root)

    root.mainloop()


if __name__ == '__main__':
    main()
