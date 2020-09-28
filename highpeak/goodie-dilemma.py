# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:12:59 2020

@author: yetur
"""
import pandas as pd
d={}
l=[]
l1=[]
print("Name of Input file:")
inputfile=input()
fin=open(inputfile,'r')
for line in fin:
    line=line.strip().split(":")
    if line!=['']:
        l.append(line)

for i in l:
    if(i[1]!=''):
        d[i[0]]=int(i[1])
res=d.copy()
res.pop('Number of employees')
#print(l)
#print(d)
#print(res)
print("Goodies and Prices:")
n=d['Number of employees']
print("Number of employees:",n)
print("\nHere the goodies that are selected for distribution are:")
for i in range(n):
    name=input()
    l1.append(name)
r=dict((k,res[k])for k in l1 if k in res)
r1=sorted(r.items(),key=lambda x:x[1])
#print(r1)
emp_goodies=pd.DataFrame(r1,columns=['Goodies','Price'])
print("\n",emp_goodies)
a=r[max(r,key=r.get)]
b=r[min(r,key=r.get)]
diff=a-b
print("\nAnd the difference between the chosen goodie with highest price and the lowest price is",diff)
outfile=open('output.txt','a')
outfile.write(f'Here the goodis that are selected for distribution are:')
outfile.write(f'\n{emp_goodies}')
outfile.write(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is: {diff}")
outfile.close()