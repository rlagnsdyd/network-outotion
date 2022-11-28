#!/bin/env python
#-*- coding: utf-8 -*-

import mylog5
import os

logfile = "/var/log/syslog"
file_length = os.path.getsize(logfile)

mylog5.printlog("/var/log/syslog", "fail", int(file_length/2), 3, 5)
