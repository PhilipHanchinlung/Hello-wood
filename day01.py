import os,sys
import numpy

print("import success")

print("numpy vesion : "+str(numpy.version.full_version))

pythonVersion = sys.version
print(pythonVersion)
# class area
# ctrl+/ = command
class boy():
    def __init__(self):
        self.gender='male'
        self.interest = "girl"
    def say(self):
        print("I am a boy!!!")
# class test
'''
Peter=boy()
print(Peter.gender)
print(Peter.interest)
Peter.say()
'''