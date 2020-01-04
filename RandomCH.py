# -*- coding: utf-8 -*-
from Xulydulieu import rand
from GetDulieu import list3
import random
def roll():
	temp= rand.randomCH()
	while (list3[temp[2]]==1):
		temp= rand.randomCH()
	list3[temp[2]]=1
	cauhoi=temp[0]
	dapandung=temp[1]
	dapan=[0,0,0,0]
	dapan[0]=dapandung
	i=0
	while (i<3):
		temp=rand.randomDAS()
		kiemtra=temp in dapan
		while (kiemtra):
			temp=rand.randomDAS()
			kiemtra=temp in dapan
		if (kiemtra==0):
			i=i+1
			dapan[i]=temp
	temp=dict()
	for i in range(4):
		temp1=random.randrange(0,1000)
		while (temp1 in temp.keys()):
			temp1=random.randrange(0,1000)
		temp[temp1]=dapan[i];
	temp2=[]
	for i in sorted(temp):
		temp2.append(temp[i]);
	dapan=temp2
	return cauhoi,dapandung,dapan
def taonganhang():
	temp=open('BankAnswer.txt','w')
	for i in range(len(list3)):
		tam=roll()
		tam1=tam[2]
		temp.write(tam[0].decode("utf-8")+'\n')
		temp.write(tam[1]+'\n')
		temp.write(tam1[0]+'\n')
		temp.write(tam1[1]+'\n')
		temp.write(tam1[2]+'\n')
		temp.write(tam1[3]+'\n')
	temp.close()