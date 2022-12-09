class Juncture:
    def __init__(self, indicator1, indicator2, indicator3, indicator4, window):
        self.indicator1 = indicator1
        self.indicator2 = indicator2
        self.indicator3 = indicator3
        self.indicator4 = indicator4
        self.window = window

        self.running = False
        self.cycles_completed = 0
        self.cycle_number = 0
        self.cycle = ''

    def traffic_lights_cycle(self):
        if self.cycles_completed % 2 == 0:
            indicator1 = self.indicator1
            indicator2 = self.indicator2
            indicator3 = self.indicator3
            indicator4 = self.indicator4
        else:
            indicator1 = self.indicator2
            indicator2 = self.indicator1
            indicator3 = self.indicator4
            indicator4 = self.indicator3

        if 0 <= self.cycle_number < 12:
            if self.cycle_number == 0:
                indicator1.turn_green_from_red()
                indicator3.turn_green_from_red()

                indicator2.turn_red()
                indicator4.turn_red()
            else:
                indicator1.turn_green()
                indicator3.turn_green()

                indicator2.turn_red()
                indicator4.turn_red()
            self.cycle_number += 1

        if 12 <= self.cycle_number:
            indicator1.turn_yellow()
            indicator3.turn_yellow()
            self.cycle_number += 1

        if self.cycle_number == 15:
            self.cycles_completed += 1
            self.cycle_number = 0

        self.cycle = self.window.after(1000, self.traffic_lights_cycle)

    def traffic_start(self):
        self.running = True
        self.traffic_lights_cycle()

    def traffic_stop(self):
        self.running = False
        self.window.after_cancel(self.cycle)
