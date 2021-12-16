#-*- coding: utf-8 -*-
#from __future__ import unicode_literals
print("Fuel consumption calculator ver. 0.2")
#source = unicode(source, 'ascii')
from datetime import datetime
now = datetime.now ()
v = float (input ("Type vol.:"))
s = float (input ("Type distance after refuel:"))
if v < 0 :
	print ("Incorrect value")
elif s < 0 :
	print ("Incorretc value")
else:
	cons = float(( v/s ) * 100 )
	round (cons)
print ('Average fuel consumption is  {:3.2f}'.format(cons) ,'l/100km')
f = open('data', 'a', encoding='utf-8')
handle = open('data', 'a')
handle.write('{:3.2f} l/100km \n'.format(cons))
handle.close()
