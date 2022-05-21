import re
terminal_expr=['!','&&','||','<','>','=','id','$']
#exp=>E exp'=>N term=>T term'=>N  Factor=>F Factor'=>M COMPOP=>C OPERAND=>O Z=>endstate badl (epi) 
nonterminal_expr=['E','N','T','W','F','M','C','O']

splitbynonterminalarray=''
print(splitbynonterminalarray)
parsetable={
    'E':{'!':'T N',
                   '&&':-1,
                   '||':-1,
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':'T N',
                   '$':-1
                   },
    'N':{'!':-1,
                   '&&':-1,
                   '||':'|| T N',
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':-1,
                   '$':'Z'},
    'T':{'!':'F W',
                   '&&':-1,
                   '||':-1,
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':'F W',
                   '$':-1},
    'W':{'!':-1,
                   '&&':'&& F W',
                   '||':'Z',
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':'F W',
                   '$':-1},
    'F':{'!':'O M',
                   '&&':-1,
                   '||':-1,
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':'O M',
                   '$':-1},
    'M':{'!':-1,
                   '&&':'Z',
                   '||':'Z',
                   '<':'C O',
                   '=':'C O',
                   '>':'C O',
                   'id':-1,
                   '$':'Z'},
    'C':{'!':-1,
                   '&&':-1,
                   '||':-1,
                   '<':'<',
                   '=':'=',
                   '>':'>',
                   'id':-1,
                   '$':-1},
    'O':{'!':'! O',
                   '&&':-1,
                   '||':-1,
                   '<':-1,
                   '=':-1,
                   '>':-1,
                   'id':'id',
                   '$':-1}          
                   }
class expr:
    def  __init__(self,name,first,follow):
        self.name=name 
        self.follow=follow
        self.first=first
    def terminal(self):
        return True if self.name in terminal_expr else False
def stringmatch(instr):
    inlist=[]
    in
    inlist=instr.split().reverse
    stackbuf=[]
    stackbuf.push(nonterminal_expr[0])



