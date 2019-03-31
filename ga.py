# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 11:51:40 2019

@author: parcham parcham  ebrahimparcham@gmail.com

this program use for ga algoritm
"""

import numpy as np
import random

class Gafun:
    
    def crossover(p1,p2):
        
        
        l1 =p1['Position'];
        l2 =p2['Position'];

        i1 = random.randrange(1,nvar);
        
        n1 = l1[0:i1]+l2[i1:];       
        n2 = l2[0:i1]+l1[i1:];
        
        return n1,n2;
        
        
        
    def mutation(p1):
        
        l1 =p1['Position'];
        l2 = l1.copy();
        i1 = random.randrange(1,nvar);
        l2[i1] = (np.max(l1)-l1[i1]);
        return l2;      

class PopCreate:
    def __init__(self):
        self.Pop =[];
    def CostF(pos):
        z = np.sum(np.power(pos,2));
        return z;
    def sortPop(self,pop):
        pop.sort(key=lambda x: x['Cost'])
        return pop;
    def createpop(self,npop):
        for i in range(npop):
            rnd = ([random.random() for i in range(nvar)]);
            cost = PopCreate.CostF(rnd);
            my_dict = {'Position':rnd,'Cost':cost}
            self.Pop.append(my_dict);
        return self.Pop;   
    
global nvar
nvar=5;
varmin = -1;
varmax = 1;

maxiter = 100;
npop = 100;

pCross = 0.8;
nCross = int(np.round(pCross * npop/2));

pMu = 0.8;
nMu = int(np.round(pCross * npop));

Pop = PopCreate();
pop = Pop.createpop(npop)
pop = Pop.sortPop(pop)
bestPop = pop[0]['Cost']

for itr in range(maxiter):
    Popc =[];
    Popm =[];
    for cross in range(int(round(nCross/2))):
        i1 = random.randrange(1,npop);
        i2 = random.randrange(1,npop);
        
        p1 = pop[i1];
        p2 = pop[i2];
        
        n1,n2 = Gafun.crossover(p1,p2);
        cost = PopCreate.CostF(n1);
        my_dict = {'Position':n1,'Cost':cost}
        Popc.append(my_dict);
        cost = PopCreate.CostF(n2);
        my_dict = {'Position':n2,'Cost':cost}
        Popc.append(my_dict);
        
    for mross in range(nMu):
        i1 = random.randrange(1,npop);
        p1 = pop[i1];
        
        n1 = Gafun.mutation(p1);
        cost = PopCreate.CostF(n1);
        my_dict = {'Position':n1,'Cost':cost}
        Popm.append(my_dict);
        
    temp = pop + Popc + Popm;
    temp = Pop.sortPop(temp)
    pop = temp[:npop];
    minum = pop[0]['Cost'];
    print('itr {0} minumcost is {1} and best cost {2}'.format(itr,minum,bestPop))
    if bestPop>minum:
        bestPop = minum;
print('-'*40)   ;    
print(pop[0]['Cost']); 
print(pop[0]['Position']);   
        
        
        
        
    
    
    
    