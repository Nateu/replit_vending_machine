import choice
import can


class VendingMachine(object):
    def __init__(self):
        self.stock = None

    def provision_with(self, my_can):
        self.stock = my_can

    def choice(self, my_choice):
        if self.stock is None:
            return can.Can.NOTHING
        if my_choice == choice.Choice.FIZZY_ORANGE:
            return can.Can.FANTA
        else:
            return can.Can.COKE
