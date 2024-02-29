# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 11:49:01 2024

@author: marcj
"""

class BasicMathOperations:
    def __init__(self,fn,ln,num1,num2):
        #initializing with first name (fn) last name (ln) and numbers
        self.fn=fn
        self.ln=ln
        self.num1=num1
        self.num2=num2
    def greet(self):
        print(f"Hello, {self.fn} {self.ln} and welcome to Basic Math Operations...")
    def sumnum(self):
        s=self.num1+self.num2
        print(f"Sum of {self.num1} and {self.num2} >>> {s}")
    def ops(self,op):
        if op=="+": #condition statement to check operation
            s=self.num1+self.num2
            print(f"Operation {self.num1} {op} {self.num2} >>> {s}")
        elif op=="-":
            s=self.num1-self.num2
            print(f"Operation {self.num1} {op} {self.num2} >>> {s}")
        elif op==":":
            s=self.num1/self.num2
            print(f"Operation {self.num1} {op} {self.num2} >>> {s}")
        elif op=="*":
            s=self.num1*self.num2
            print(f"Operation {self.num1} {op} {self.num2} >>> {s}")
        else:
            print(f"Operation {op} not available...")
    def calculateSquare(self):
        s=(self.num1)**2
        print(f"Square of {self.num1} >>> {s}")
    def fact(self):
        #factorials can only be executed with Natural numbers
        self.num1=round(self.num1) #round number to above decimal
        print(f"If is decimal number rounded to integer >>> {self.num1}")
        s=1
        f=self.num1
        if self.num1>0: #only with positive numbers
            while f!=0: #loop to compute factorial
                s=s*f #multiplies successively
                f=f-1 #from one number to the other, single indentations
            print(f"Factorial of {self.num1} >>> {s}")
        else:
            print(f"Factorial of {self.num1} not available, for negative numbers...")
    def count(self):
        #each number have to be integer to make single count indentations
        #instead of numerous decimal ones
        self.num1=round(self.num1)
        self.num2=round(self.num2)
        d=abs(abs(self.num1)-abs(self.num2)) #distance as absolute value of difference
        print("If either number is negative, will compute distance between both as absolute value...")
        print("Decimals also rounded to greater integer...")
        #condition statement to compare each and assign end boundary to bigger number
        if abs(self.num1)>abs(self.num2): 
            s=abs(self.num2)
            e=abs(self.num1)
        else:
            s=abs(self.num1)
            e=abs(self.num2)
        l=[] #list for count
        while d!=0:
            l.append(s+d) #appends number added to end bound value
            d=d-1 #indentations of 1 between each count
        l.sort() #sort list for natural order
        print(f"Count list from start {s} till end {e} is >>> {l}")
    def calculateHypotenuse(self):
        #abs not needed because values are squared by calc square method
        h=(self.calculateSquare(self.num1)+self.calculateSquare(self.num2))**0.5
        h=round(h,2) #round value in case of many decimal cases
        print(f"With sides of {self.num1} and {self.num2} hypotenuse >>> {h}")
    def rect(self):
        #absolute values, cannot have negative lengths
        w=abs(self.num1)
        l=abs(self.num2)
        a=l*w
        a=round(a,2) #round value in case of many decimal cases
        print(f"With width of {w} and length of {l} area of rectangle >>> {a}")
    def power(self):
        p=self.num1**self.num2
        print(f"{self.num1} to the power of {self.num2} is >>> {p}")
    def argt(self):
        print("Type of argument >>> "+str(type(self.num1)))

def main():
    i=BasicMathOperations("Marc", "Jalkh", 4, 78)
    d={"greet":0,"sum":1,"operations":2,"square":3,"factorial":4,"count":5,"hypotenuse":6,"rectangle":7,"power":8,"argtype":9}
    print("Numbered operations >>> "+str(d))
    o=int(input("Select task number from 0 to 9 >>>  "))
    while o<0 or o>9: #check for task key existence and prompts replacement
        o=int(input("Select task number from 0 to 9 >>>  "))
    if o==0: #list of condition statement for each task respective to its key number
        i.greet()
    elif o==1:
        i.sumnum()
    elif o==2:
        #user input of operation type per method argument
        opp=str(input("Select operation >>> "))
        i.ops(opp)
    elif o==3:
        i.calculateSquare()
    elif o==4:
        i.fact()
    elif o==5:
        i.count()
    elif o==6:
        i.calculateHypotenuse()
    elif o==7:
        i.rect()
    elif o==8:
        i.power()
    elif o==9:
        i.argt()
main()

#fact-count-absolutevals