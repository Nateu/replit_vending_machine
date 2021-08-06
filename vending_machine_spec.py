from mamba import description, context, it, before
from expects import expect, equal

import vending_machine
import choice
import can
'''
We have a vending machine that will not take payments and
that will give back one of three drinks based on a choice.
'''

with description('Given a vending machine') as self:
    with before.each:
        self.my_vending_machine = vending_machine.VendingMachine()

    with context('that is empty'):
        with context('When I ask for a fizzy orange'):
            with it('Should return nothing'):
                expect(
                    self.my_vending_machine.choice(
                        choice.Choice.FIZZY_ORANGE)).to(equal(can.Can.NOTHING))

    with context('that is stocked'):
        with context('When I ask for a fizzy orange'):
            with it('Should return a Fanta'):
                self.my_vending_machine.provision_with(can.Can.FANTA)
                expect(
                    self.my_vending_machine.choice(
                        choice.Choice.FIZZY_ORANGE)).to(equal(can.Can.FANTA))

        with context('When I ask for a cola drink'):
            with it('Should return a Coke'):
                self.my_vending_machine.provision_with(can.Can.COKE)
                expect(self.my_vending_machine.choice(choice.Choice.COLA)).to(
                    equal(can.Can.COKE))
