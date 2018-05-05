"""
Lidar
"""

import time
import numpy as np


class B0602Lidar():
    def __init__(self, port='/dev/ttyUSB0'):
        #from rplidar import RPLidar
        from donkeycar.parts.B0602Lidar import B0602Lidar
        self.port = port
        self.frame = np.zeros(shape=365)
        self.lidar = B0602Lidar(self.port)
        #self.lidar.clear_input()
        time.sleep(1)
        self.on = True


    def update(self):
        self.measurements = self.lidar.iter_measurements()
        for new_scan, quality, angle, distance in self.measurements:
            print("angle: {angle}, distance: {distance}".format(angle=angle, distance=distance))
            angle = int(angle)
            if angle < 365:
                self.frame[angle] = 2*distance/3 + self.frame[angle]/3
            if not self.on: 
                break
            
    def run_threaded(self):
        return self.frame
