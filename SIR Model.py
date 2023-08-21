#!/usr/bin/env python
# coding: utf-8

# In[66]:


# Atirek Aryan 200221
r=3.65 #Basic Reproductive  Ratio
h=0.25 #grid size
b=1.66 #transmission rate
g=b/r #recovery rate
g


# In[67]:


# Creating arrays for S, I and R fractional values
s=[]
s.append(762/763)
i=[]
i.append(1/763)
r=[]
r.append(0/763)


# In[68]:


#Running a while loop to compute successive values for the S, I and R 

c=0
while(1):
    s1=(0-b*s[c]*i[c])
    i1=(b*s[c]*i[c]-g*i[c])
    r1=(g*i[c])
    s2=0-b*(s[c]+h*s1/2)*(i[c]+h*i1/2)
    i2=b*(s[c]+h*s1/2)*(i[c]+h*i1/2)-g*(i[c]+h*i1/2)
    r2=(g*(i[c]+h*i1/2))
    s3=0-b*(s[c]+h*s2/2)*(i[c]+h*i2/2)
    i3=b*(s[c]+h*s2/2)*(i[c]+h*i2/2)-g*(i[c]+h*i2/2)
    r3=(g*(i[c]+h*i2/2))
    s4=0-b*(s[c]+h*s3/2)*(i[c]+h*i3/2)
    i4=b*(s[c]+h*s3/2)*(i[c]+h*i3/2)-g*(i[c]+h*i3/2)
    r4=(g*(i[c]+h*i3/2))
    s.append(s[c]+h*(s1+2*s2+2*s3+s4)/6)
    i.append(i[c]+h*(i1+2*i2+2*i3+i4)/6)
    r.append(r[c]+h*(r1+2*r2+2*r3+r4)/6)
    c=c+1
    if(i[c]<1/763):
        break
    
    


# In[69]:


import matplotlib.pyplot as plt
import numpy as np


# In[70]:


#Creating array for time
t=np.linspace(0,22.25,num=89)


# In[80]:


#Plotting S,I and R according to the  data calculated
plt.plot(t, s, 'r', label="Susceptible") 
plt.plot(t, i, 'b', label="Infected") 
plt.plot(t, r, 'g', label="Recovered")
plt.legend()
plt.xlabel("Time (in Days)")
plt.ylabel("S, I, R")
plt.show()


# In[72]:


#Finding maximum value for Infected Group
max=0
for j in range(89):
    if(i[max]<i[j]):
        max=j
max 


# In[73]:


i[26]*763


# In[74]:


#Finding the 1% of the maximum Infected value
op=0
for j in range(26,89):
    if(i[26]*0.01>i[j] or i[26]*0.01==i[j] ):
        op=j
        break


# In[75]:


op


# In[76]:


i[26]


# In[77]:


i[77]


# In[78]:


i[76]


# In[79]:


#Time taken to reach the 1%  from Maximum
time=(77-26)*0.25
time

