#math_quiz_ver2
#also does addition, subtraction division and multiplication of integers

##########
#IMPORTS#
##########

from time import time
from random import randint

#########
#functions#
#########


def question (a,b,ops):

	return null

def operator (arg):
	switcher = {
        	0: "+",
        	1: "-",
        	2: "*",
		3: "/",
    	}
	return switcher[arg]


###start of main 
#get two random numbers
a = randint(0,1000)
b = randint(0,1000)

#get randomly decide what operation do to
#print(randint(0,3))
ops= operator(randint(0,3))

question(a,b,ops)


