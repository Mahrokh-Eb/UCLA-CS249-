#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''there are two functions, QuickCheck and isValidString. The code needs "s" to run the function. 
If the code doesn't pass QuickCheck, it doesnt get throgh isValidString. 
however, QuickCheck is called in isValidString. 
'''
# first check to see if s is invalid, check the rest of charectors
def QuickCheck(s):
    isValid = True
    l=len(s)
    
    # first check if my string has a lenght of zero
    if l==0:
        isValid = False
        
    # if first char is not Q (s[0] !=s.capitalize()[0])
    elif s[0] != 'Q' :
        isValid = False
            
    # if is not alphabet or number 
    elif  not s.isalnum():
        isValid = False
    
    #if contain P or D in caps or lower case
    elif 'P' in s or 'D' in s  or 'q' in s:
        isValid = False
        
    # check if last char is digit
    elif not s[l-1].isdigit():
        isValid = False

    return isValid

# starting main function
def isValidString(s): 
    
    isValid = True
    isValid = QuickCheck(s)
    
    if isValid:
        #split Q from the code
        s_splited = s.split('Q')
        # split the rest of the char
        s_splited = s_splited[1:]

        for part in s_splited:
            # if p come sooner than d 
            Q_sum = part.split('p')
            # id d come sooner than p 
            Q_sumAlt= part.split('d')
            # when p or d don’t have any digit number, it gives spilit error. it is shown by try-except on error be not valid
            try:
                #check if only one defect and pass 
                if len(Q_sumAlt) == 2 and len(Q_sum)== 2 and not 'd' in Q_sum[0] :  
                    # Q = Q_sum[0]  and  d Q_sumAlt[1]
                    q= Q_sum[0]
                    d= Q_sumAlt[1]
                    p= Q_sum[1].split('d')[0]
                
                else : 
                    # Q = Q_sumAlt[0]  and  p Q_sum[1]
                    q= Q_sumAlt[0]
                    p= Q_sum[1]
                    d= Q_sumAlt[1].split('p')[0]
            
            
                # to make sure no other alphabet(@!%,,,) or number is in it 
                if  q !='0' and len(q) >0 and len(p) >0 and len(d) >0 and p.isdigit() and d.isdigit() and q.isdigit():
                    # valid sum
                    if int(q) == int(d)+ int(p) :
                            # not leading zero
                            if  (len(q)>1 and q.startswith('0')) or (len(d)>1 and d.startswith('0')) or (len(p)>1 and p.startswith('0')):
                                isValid = False
                    else:
                        isValid = False
                else:
                    isValid = False
            except:
                isValid = False
                        
    return isValid


# In[ ]:




