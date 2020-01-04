# encoding: utf-8
from GetDulieu import dictionary
import random

class Xuli:
	'This is Correct'
	def __init__(self,dictionary):
		self.key=list(dictionary.keys())
		self.value=list(dictionary.values())
		self.dictionary=dictionary
	def key(self):
		return self.key
	def value(self):
		return self.value
	def randomCH(self):
		temp=random.randrange(-1,len(self.key))
		return self.key[temp],self.value[temp],temp
	def randomDAS(self):
		temp=random.randrange(-1,len(self.value))
		return self.value[temp]
rand=Xuli(dictionary)