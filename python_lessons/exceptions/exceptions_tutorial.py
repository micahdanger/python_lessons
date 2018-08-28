#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2018/08/13

@author: Micah Beckman
"""

import logging
import time

# Create logger
logging.basicConfig(filename="problems.log", level=logging.DEBUG)

logger = logging.getLogger()


def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required"""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))


data = read_file_timed("/Users/micahbeckman/chickenwings.png")

