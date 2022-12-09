class TrafficIndicator:
    def __init__(self, indicator_box, green_light,
                 yellow_light, red_light, canvas):
        self.indicator_box = indicator_box
        self.green_light = green_light
        self.yellow_light = yellow_light
        self.red_light = red_light
        self.canvas = canvas

        self.box = canvas.create_rectangle(self.indicator_box, fill='#5A5A5A')
        self.green = canvas.create_oval(self.green_light, fill='#D3D3D3')
        self.yellow = canvas.create_oval(self.yellow_light, fill='#D3D3D3')
        self.red = canvas.create_oval(self.red_light, fill='red')

    def turn_green_from_red(self):
        self.canvas.delete(self.green)
        self.canvas.delete(self.yellow)
        self.canvas.delete(self.red)

        self.canvas.create_oval(self.green_light, fill='#D3D3D3')
        self.canvas.create_oval(self.yellow_light, fill='yellow')
        self.canvas.create_oval(self.red_light, fill='red')

    def turn_green(self):
        self.canvas.delete(self.green)
        self.canvas.delete(self.yellow)
        self.canvas.delete(self.red)

        self.canvas.create_oval(self.green_light, fill='green')
        self.canvas.create_oval(self.yellow_light, fill='#D3D3D3')
        self.canvas.create_oval(self.red_light, fill='#D3D3D3')

    def turn_yellow(self):
        self.canvas.delete(self.green)
        self.canvas.delete(self.yellow)
        self.canvas.delete(self.red)

        self.canvas.create_oval(self.green_light, fill='#D3D3D3')
        self.canvas.create_oval(self.yellow_light, fill='yellow')
        self.canvas.create_oval(self.red_light, fill='#D3D3D3')

    def turn_red(self):
        self.canvas.delete(self.green)
        self.canvas.delete(self.yellow)
        self.canvas.delete(self.red)

        self.canvas.create_oval(self.green_light, fill='#D3D3D3')
        self.canvas.create_oval(self.yellow_light, fill='#D3D3D3')
        self.canvas.create_oval(self.red_light, fill='red')
