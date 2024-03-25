import matplotlib.pyplot as plt
import numpy as np

amount = 20
pstime = 0.02
temp = 0
list = np.random.randint(0,80,amount)
t = np.arange(0, amount, 1)

n = len(list)
def mergesort(arr):
   
    if len(arr) > 1:    
        middle = n/2    
        
        leftside = arr[:middle]
        rightside = arr[middle:]
        
        mergesort(leftside)
        mergesort(rightside)
        
        i=0
        o=0
        
        
        while i < len(leftside) and o < len(rightside):
            if leftside[i] <= rightside[o]:
                arr[temp] = leftside[i]
                i+=1
            else:
                arr[temp] = rightside[o]
                o+=1
            temp+=1
            plt.bar(list(range(amount)), arr)
            plt.pause(pstime)
            plt.clf()
        
        while i < len(leftside):
            arr[temp] = leftside[i]
            i += 1
            temp += 1
            plt.bar(list(range(amount)), arr)
            plt.pause(pstime)
            plt.clf()
        
        while o < len(rightside):
            arr[temp] = rightside[o]
            o += 1
            temp+=1
            plt.bar(list(range(amount)), arr)
            plt.pause(pstime)
            plt.clf()
        

if __name__ =='main':
    print(list)
    mergesort(list) 
        
        
        
        
        
            
        
    
        
    
    
    
        

        
        
    
        
        
