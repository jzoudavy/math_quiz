from time import time
from random import randint
a = randint(0,1000)
b = randint(0,1000)
cor_answer = a+b
usr_answer = input("what is "+str(a)+"+"+str(b)+"? \n")
start = time()
if usr_answer == cor_answer:
	print("yes you are correct!")
else:
	print("no you are wrong!")
end = time()
elapsed = end -start

print("That took you"+str(elapsed)+" seconds. \n")
	
	