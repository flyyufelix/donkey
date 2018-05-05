#!/usr/bin/env python3

'''Records measurements to a given file. Usage example:

$ ./record_measurements.py out.txt'''
import sys
from B0602Lidar_v2 import B0602Lidar


PORT_NAME = '/dev/ttyUSB0'


def run(path):
    '''Main function'''
    lidar = B0602Lidar(port=PORT_NAME)
    outfile = open(path, 'w')
    try:
        print('Recording measurements... Press Crl+C to stop.')
        for measurement in lidar.iter_measurements():
            line = '\t'.join(str(v) for v in measurement)
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    #lidar.stop()
    #lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    run(sys.argv[1])
