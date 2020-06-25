from os import system
from datetime import datetime
from json import load, dump
import fitur5atribut

statload = fitur5atribut.loadstat()

if statload:
	fitur5atribut.loginpas()
	sleep(2)
	print("Login succesful")