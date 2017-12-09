
# coding: utf-8

# In[1]:

#libraries
import scipy.stats as stat
import numpy as np
from __future__ import division
import math


# Question 1

# Part D

# In[3]:

#Function for the mean of the negative binomial distribution
def MeanNegBin(alpha,p):
    return alpha*p/(1-p);
#Function for the variance of the negative binomial distribution
def VarNegBin( alpha,p ):
    return alpha*p/((1-p)**2);


# Part E

# In[4]:

alpha=4
p=2/3
print VarNegBin(alpha,p)
print MeanNegBin(alpha,p)


# Question 6

# Part A

# In[5]:

#Function for the mean of S
def MeanS( alpha,p,l ):
    return l*alpha*p/(1-p);
#Function for the variance of S
def VarS( alpha,p,l ):
    return l*alpha*p/(1-p)+(l**2)*alpha*p/((1-p)**2);


# Part B

# In[6]:

#Function for the mean of P(S=0)
def pS0( alpha,p,l ):
    return ((1-p)/(1-p*np.exp(-l)))**(alpha);


# Part C

# In[9]:

#Function for the mean of P(S=j), j >= 1
def pSj( alpha,p,l,j ):
    #Create an empty list
    List1=[]
    #P(S=0) as first element of the previous empty list
    List1.append(pS0(alpha,p,l))
    #For loop
    for i in range(1,j+1,1):
    #Build a list with general term from panjer recursion
        List2=[(p+p*(alpha-1)*k/i)*np.exp(-l)*(l**k)
                /math.factorial(k)*List1[i-k]
        for k in range(1,i+1,1)]
        #Summing the element of the vector to get P(S=i)
        List1.append(sum(List2))
    #Returning the jth element of the vector which is P(S=j)
    return List1[j]/(1-p*np.exp(-l));


# Part D

# In[10]:

#Parameters
alpha=4
p=2/3
l=5
j=40
print MeanS( alpha,p,l )
print VarS( alpha,p,l )
print pS0( alpha,p,l )
print pSj( alpha,p,l,j )

