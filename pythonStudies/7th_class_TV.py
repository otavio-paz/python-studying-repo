class TV:  # a method, it doesnot return a value
    def __init__(self):
        self.turnon = False
        self.channel = 5
    def power(self):
        if self.turnon:
            self.turnon = False
        else:
            self.turnon = True

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        self.channel -= 1


tv = TV()
print('TV is turned on: {}'.format(tv.turnon))
tv.power()
print('TV is turned on: {}'.format(tv.turnon))
tv.power()
print('TV is turned on: {}'.format(tv.turnon))

print('Current channel: {}'.format(tv.channel))
tv.channel_up()
tv.channel_up()
print('Current channel: {}'.format(tv.channel))
tv.channel_down()
print('Current channel: {}'.format(tv.channel))