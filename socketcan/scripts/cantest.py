#!/usr/bin/python
import time
import can
import os
from threading import Timer

#-------pack and send can frams------#
def can0send(MsgID):

    bus = can.interface.Bus(channel='can0', bustype='socketcan')
    msg = can.Message(arbitration_id=MsgID, data=[1, 2, 3, 1, 3, 1, 4, 1], is_extended_id=False)
    bus.send(msg)

class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)

if __name__ == '__main__':

    print('Pin Configuring')
    os.system('sh /home/debian/myProject/caninit_loopbackon')
    print('Pin Configure Finished')

    print('sending can message now')
    t = RepeatingTimer(1 , can0send,(0x300,))
    t.start()