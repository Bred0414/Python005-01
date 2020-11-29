#!/usr/bin/env python3

import logging
import time
import os

CurrentDay = time.strftime('%Y-%m-%d')
FilePath = '/var/log/python-{}'.format(CurrentDay)


def log():
    if not os.path.exists(FilePath):
        os.makedirs(FilePath)

    os.chdir(filePath)
    logging.basicConfig(filename='xxxxx.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-6s %(levelname)-8s '
                               '[line: %(lineno)d] %(message)s'
                        )
    logging.debug('The funtion of log() has been called')


if __name__ == '__main__':
    log()
