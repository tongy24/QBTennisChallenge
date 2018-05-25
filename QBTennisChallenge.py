# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### Based on http://www.quantbet.com/quiz/quant
### Works out the probability of winning the set given the probability
### of winning a point.
#P= Prob Djokovic wins a point; 
#D= Number of games won by Djokovic;
#M= Number of games won by Murray
from math import factorial
def prob_win_set(P,D,M):
    Q= 1-P
    #Probability of winning a game:
    G = (P**4) +(4*(P**4)*Q) + (10*(P**4)*(Q**2)) + ((20*(P**5)*(Q**3))/(1- 2*P*Q))
    #Probability of winning set 
    if D>M:
        S = (G**(D))*((1-G)**M)* (factorial(D+M-1)/(factorial(D-1)*factorial(M)))
    else:
        S = (G**(D))*((1-G)**M)* (factorial(D+M-1)/(factorial(D)*factorial(M-1)))
    print(S)
#Example where Djokovic beats Murray in a point with p=0.49
#Set currently stands at 4-6
prob_win_set(0.49,4,6)