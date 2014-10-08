import random as random1
def reset(percent):   
   return random1.randrange(100) < percent
a = [reset(70) for x in range(100)]

a = []
seedvalue="abc"
random1.seed(seedvalue)
for i in range(0,100):
    if burst_count < 4:
    
        if reset() != True:
            a.append(False)
        else
            random1.seed(seedvalue)
            a.append(True)
            burst_count=0

index = 0;
for item in a:
    if item is True:
        index = index+1

print index
