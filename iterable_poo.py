#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:02:14 2023

@author: efamouzou
"""

class S:
    def __init__(self,c):
        self.c = c

    def __getitem__(self,t):
        n = len(self.c)
        i=0
        while i<n:
            if self.c[i]==t:
                return i
            i += 1
        return -1


if __name__=='__main__':
    s = S("Hello World !")
    print(s['e'], end=" ")  # indice du premier 'e'
    print(s['o'], end=" ")  # indice du premier 'o'
    print(s['!'], end=" ")  # indice du premier '!'
    print(s['x'], end=" ")  # pas de x dans s
    
    #exo2####################################
    
class Diviseurs:
    def __init__(self,n):
        self.n = n
        
    def __getitem__(self,i):
        i+=1
        if i>self.n : raise IndexError("l'index est hors des limites")
        return self.n % i == 0


if __name__=='__main__':
    d12 = Diviseurs(12)
print(f"{d12[4]}, {d12[7]}")

##exo2-b###################################


class Diviseurs(int) :
    def __init__(self,val):
        self.val=val
        
    def __getitem__(self,i) :
        if i>self.val : 
            raise IndexError("Valeur supérieure à l'entier")
        elif i>0 :
            return self.val%i==0
        else : 
            return False
        
        
if __name__=='__main__':
  d12 = Diviseurs(12)

for i in d12:
    print(i,end=" ") # False True True True True False True False False False False False True

for i,d in enumerate(Diviseurs(100)):
  if d:
    print(i,end=" ") # 1 2 4 5 10 20 25 50 100   
    
    
    #####################################
    
    
## itérateurs    
class Diviseurs():
    def __init__(self,n):
        self.n = n
class it():
    def __init__(self,d):
        self.diviseurs = d
        self.i=0
        
    def __next__(self):
        if self.i == self.diviseurs.n :
            raise StopIteration
        self.i+=1
        while self.diviseurs.n % self.i != 0:
            self.i+=1
        return self.i
    def __iter__(self):
        return self
    
    
if __name__=='__main__':        
  d = Diviseurs(50)
it1 = it(d)
for i in it1:
 it2 = it(d)
 for j in it2:
    print(f"({i},{j})", end=" ")    
    
  ###############################################  
    
class Diviseurs():
    def __init__(self,k):
        self.k = k

    def __iter__(self):
      return self.It(self)

    class It():
      def __init__(self,d):
        self.diviseurs = d
        self.i = 0

      def __next__(self):
        if self.i == self.diviseurs.k:
          raise StopIteration()

        self.i += 1
        while self.diviseurs.k % self.i != 0 :
          self.i += 1
        return self.i

      def __iter__(self):
        return self
 
########### Context manager

### difference entre les deux codes

try:
  with open('data', 'w') as mon_fichier: 
    for i in range(-10,10):
      print(1/i, file=mon_fichier)
except: ZeroDivisionError
print(mon_fichier.closed)
      
      
try:     
  mon_fichier = open("data", "w")
  for i in range(-10,10):
    print(1/i, file=mon_fichier)
  mon_fichier.close()
except: ZeroDivisionError
print(mon_fichier.closed)
 

#exo cm
class Balise():
    def __enter__(self):
        print("<balise>")
    def __exit__(self,type,value,traceback):
        print("</balise>")
    def print(self,msg):
        print(msg)
with Balise():
    print("Hello",end=" ")
    print("World !",end="\n")
     
print(mon_fichier.closed)


####n*2
class Balise():
    #def __init__(self,s):
        #self.s=s
    def __enter__(self):
        print("<balise>")
        return self
    def __exit__(self,type,value,traceback):
        print("</balise>")
    def print(self,msg):
        print(msg)   
with Balise() as ma_balise:
    ma_balise.print("Hello")
    ma_balise.print("World !")
######################
class Balise():
    def __init__(self,arg):
        self.arg=arg
    def __enter__(self):
        print(f"<{self.arg}>")
        return self
    def print(self,txt):
        print(txt)   
    def __exit__(self,type,value,traceback):
        print("<{self.arg}>")

with Balise("parapgraphe") as ma_balise:
     ma_balise.print("Hello")
     ma_balise.print("World !")

with Balise("chapitre") as c1:
  with Balise("titre") as t1:
    t1.print("Titre du chapitre 1")
  with Balise("paragraphe") as p1:
    p1.print("Phrase 1.")
    p1.print("Phrase 2.")
  with Balise("paragraphe") as p2:
    p2.print("Phrase 1.")
    p2.print("Phrase 2.")
#################################################
import time

class Top:
    def __enter__(self):
        self.t0 = time.time()
    def __exit__(self):
        self.t1 = time.time()
    def __elapsed__(self):