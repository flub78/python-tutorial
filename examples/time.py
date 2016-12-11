#!/usr/bin/python
# -*- coding:utf8 -*

import time

print "Time and date"

# time since Epoch
t0 = time.time()
time.sleep(2)
t1 = time.time()
print t0, t1, t1 - t0

local_time = time.localtime()
print "local: \n", local_time
print time.gmtime()

print time.strftime("%Y %M %D", local_time)

print "bye"

