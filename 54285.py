def division(a , b):
    if a%b == 0:
        return True
        

n = 0        
for i in range(1,201):
    if (division(i,2) or division(i,3) or division(i,5)) and (not division(i,7)):
       #print(i)
       n+=1
       
print("Question 1   n = ",n) 

        
n = 0        
for i in range(1,201):
    if (division(i,2) or division(i,3) and (not division(i,5))) and (not division(i,7)):
       #print(i)
       n+=1
       
print("Question 2   n = ",n)       

n = 0        
for i in range(1,201):
    if (division(i,2) and(not division(i,3)) and (not division(i,5))) and (not division(i,7)):
       #print(i)
       n+=1
       
print("Question 3   n = ",n)       
