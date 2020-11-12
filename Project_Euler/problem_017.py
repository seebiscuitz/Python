# Problem: 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used? 
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use 
# of "and" when writing out numbers is in compliance with British usage.
#

import time, math
s=time.time()

odds={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
70:'seventy',80:'eighty',90:'ninety'}
sum=0

def num2words(n):
	#takes the input and converts to array of ints.
	k=[int(s) for s in str(n)]
	if len(k)==4:
		if (n%1000)==0:
			return str(odds[k[0]])+"thousand"
		else:
			return str(odds[k[0]])+"thousand"+str(num2words(n%1000))
	if len(k)==3:
		if (n%100)==0:
			return str(odds[k[0]])+"hundred"
		else:
			return str(odds[k[0]])+"hundredand"+str(num2words(n%100))
	if len(k)==2:
		if (n%10==0) or n<20:
			return str(odds[n])
		else:
			return str(odds[k[0]*10])+str(num2words(k[-1]))
	else:
		return str(odds[k[-1]])

for i in xrange(1,1001):
	sum+=len(num2words(i))

print sum
print time.time()-s