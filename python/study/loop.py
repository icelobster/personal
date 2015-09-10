#!/usr/bin/env python
import logging
import threading
from subprocess import Popen, PIPE
import subprocess
__author__ = 'dalongxia'

print("Hello")
print("Hello world!")

#class User:
#    name = ""
#    __number = 0
#
#    def __init__(self, name):
#        self.name = name
#
#    def SayHello(self):
#        print("My name is: " + self.name + " number is: " + str(self.__number))
#
#
#tom = User("tom")
#tom.SayHello()
#
#logging.warning("This is a warning.")
#logging.basicConfig(level=logging.DEBUG)
#logging.debug("This is a debug")

#print("subprocess")
#process = Popen(["ls", "-alh"], stdout=PIPE, stderr=PIPE)
#stdout, stderr = process.communicate()
#process.wait()
#print(stdout)
#
#print("subprocess1")
#subprocess.call(["ls", "-alh"])
#
#print("subprocess2")
#s = subprocess.check_output(["echo", "Hello"])
#print(s)

print("Thread")
class MyThread(threading.Thread):
    __x = 0

    def __init__(self, x):
        self.__x = x
        threading.Thread.__init__(self)

    def run(self):
        print("Thread [" + str(self.__x) + "] is running.")

for x in range(0, 10):
    MyThread(x).start()

def hello():
    print("Hello")

t = threading.Timer(10.0, hello)
t.start()