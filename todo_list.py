# -*- coding: utf-8 -*-
"""
Assignment04_Jalkh
python-collaboration
todo_list.py
"""
l=["CS HW","SW HW","DefEq Quiz","ME HW","end_list"]
t=int(input("Select number of operations> "))
c=0
while c<t:
    a=str(input("Select task> "))
    if a=="view":
        print(l)
    elif a=="new":
        i=str(input("Insert new task> "))
        l.insert(len(l)-1,i)
    elif a=="mark":
        i=str(input("Insert task to mark> "))
        if i in l and l[l.index(i)+1]!="✓":
            l.insert(l.index(i)+1,"✓")
    elif a=="delete":
        print("marked tasks>>>")
        for i in range(0,len(l),1):
            if l[i]=="✓":
                print(l[i-1])
        i=str(input("Insert completed task> "))
        if i in l:
            del l[l.index(i)+1]
            l.remove(i)        
    else:
        print("unavailable task...")
    c=c+1

"""
Assignment04_Jalkh
python-collaboration
priority_list.py
"""
#this function sorts tasks based on user priority (no markings)
def prio(l):
    print("The list is oredered as such> "+str(l))
    print("Based on the above order set priorities as numbers (1 as highest priority)>>>")
    p=[]
    pl={}
    for i in range(0,len(l)-1,1):
        print("Set priority for task "+l[i]+"> ")
        pn=int(input())
        p.append(pn)
    for i in range(0,len(l)-1,1):
        pl[l[i]]=p[i]
    print("Numbered todo list "+str(pl))
prio(l)