import random as r
#random.seed(0)# the starting value is the seed
# from random import randint, random,uniform# or * for importing everything
# randit=r.randint(0,10)#start and end
# print(randit)

# randFloat =r.random() #0.0<=Notincludig<1.0
# print(randFloat)

# randuni=r.uniform(1,11)
# print(randuni)

simpleList=[1,3,5,7,9]
pickElement=r.choice(simpleList)
print(pickElement)
print(simpleList)
r.shuffle(simpleList)
print(simpleList)