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