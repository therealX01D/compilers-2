from unicodedata import name
import ParsingT
import tokenizer
import networkx as nx
import pandas as pd
class node:
    name=""
    adjacentlist=[]
    def __init__(self,name):
        self.name=name
        self.adjacentlist=[]
    def add2adjacentlist(self,node):
        self.adjacentlist.append(node)

class tree:
    listofnodes=[]
    def __init__(self,listofnodes):
        self.listofnodes=listofnodes
    def getnode(self,str):
        return self.listofnodes[str]
    def getedgelist(self):
        edgelist=[]
        for i in range(len(self.listofnodes)):
            for j in range(len(self.listofnodes[i].adjacentlist)):
                edgelist.append((self.listofnodes[i].name,(self.listofnodes[i].adjacentlist)[j]))
        return edgelist

def checkinput(inputstring):
    intokenlist=tokenizer.token(inputstring)
    intokenlist.append("$")
    intokenlist.reverse()  
    currstate="EXP"
    nextstate=None
    listforptree=[]
    listforast=[]
    currast="$"
    level=1
    #headnode.add2adjacentlist("EXP'",TERM)
    statelist=["$","EXP"]
    while True:
        if len(statelist)==1 and len(intokenlist)==1 and statelist[0]=="$" and intokenlist[0]=="$" :
            print("--------------------------------------------------")
            for i in range(len(listforptree)):
                 print(listforptree[i].name)
                 print(listforptree[i].adjacentlist)
            print("--------------------------------------------------")
            retree=tree(listforptree)
            return "accepted",retree,listforast
        tupeoftokenizer=intokenlist[-1]
        typeofstart=tupeoftokenizer[0]
        currstate=statelist.pop()
        currstatenode=node(currstate)
        if currstate==typeofstart:
            if(currstate=="id"):
                currstatenode.add2adjacentlist(tupeoftokenizer[1])
                listforptree.append(currstatenode)
            listforast.append({currstate:level})
            intokenlist.pop()
            print(intokenlist)
            print(statelist)
            continue
        print(typeofstart)
        nextstate=ParsingT.ruletranslation(ParsingT.parsingTable(currstate,typeofstart))
        if nextstate=="EPI":
             currstatenode.add2adjacentlist("EPI")
             listforptree.append(currstatenode)
             print(statelist)
             continue
        if nextstate==-1:
             print(currstate)
             return "refused",[],[]
        templist=nextstate.split(" ")
        templist.reverse()
        for i in range(len(templist)):
            statelist.append(templist[i])
        level+=1
        templist.reverse()
        for i in range(len(templist)):
            currstatenode.add2adjacentlist(templist[i])
            #node(templist[i],currstate)
        templist.reverse()
        listforptree.append(currstatenode)
        print(statelist)
        print(intokenlist)
    print("+++++++++++++++++++++++++")
    print(listforastast)
    print("+++++++++++++++++++++++++")
#def genast(parsetree,listofterminals):
#   currnode=parsetree.listofnodes[0]
#   while currnode.name not in ParsingT.terminal_expr:

state,restree,asttree = checkinput("x<y||z>u")
print(restree)
print(asttree)