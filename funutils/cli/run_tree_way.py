import random, time

r=random.randrange(100)
pre_a = None 
cmpa =  lambda i : pre_a[i] or pre_a[i+1] or pre_a[i+2] or random.randrange(300) == 150

cnt = 0 
while 1 :
    time.sleep(0.1)
    a = [ random.randrange(100) for n in range(70) ]
    
    if pre_a : 
        a = [ 1 if (r%2) == 0 else 0  for r in a  ]
        a = [ 1 if r and cmpa(i) else 0  for i, r in enumerate(a) ]
    else : 
        a = [ 1 if (r%2) == 0 else 0  for r in a  ]
        
    m = "".join(map( str, a ))
    if not "1" in m : break 
    print( m.replace("0", " ").replace("1","C") )
    pre_a = [0]  + a  + [0]  
    cnt += 1 
    
print(cnt) 