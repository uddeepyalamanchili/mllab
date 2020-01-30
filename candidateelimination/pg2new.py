import numpy as np 
import pandas as pd 
data = pd.DataFrame(data=pd.read_csv('candidate.csv')) 
concepts = np.array(data.iloc[:,:-1])
print(concepts) 
target = np.array(data.iloc[:,-1])  
print(target)
spec_h=concepts[0]
print(spec_h)
gen_h = [["?" for i in range(len(spec_h))] for i in range(len(spec_h))]     
print(gen_h) 
    
for i, h in enumerate(concepts): 
    if target[i] == "yes": 
        for x in range(len(spec_h)): 
            if h[x]!= spec_h[x]:                    
                spec_h[x] ='?'                     
                gen_h[x][x] ='?'
            print(spec_h)
    print(spec_h)
    if target[i] == "no":            
        for x in range(len(spec_h)): 
            if h[x]!= spec_h[x]:                    
                gen_h[x][x] = spec_h[x]                
            else:                    
                gen_h[x][x] = '?'        
    print(" steps No",i+1)
    print("Specific Boundary")        
    print(spec_h)
    print("Generic Boundary")         
    print(gen_h)
        
    
indexes = [i for i, val in enumerate(gen_h) if val == ['?', '?', '?', '?', '?', '?']]    
for i in indexes:   
    gen_h.remove(['?', '?', '?', '?', '?', '?'])
print("Final Solution")
print(spec_h)         
print(gen_h)


