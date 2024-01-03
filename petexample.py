class pet:
    def __init__(self,n,a,h,p):
        self.name=n
        self.age=a
        self.hunger=h
        self.playful=p
        
    #getters
    def getName(self): #get function
        return self.name
    def getage(self):
        return self.age
    def gethunger(self):
        return self.hunger
    def getplayful(self):
        return self.playful
    #setters
    def setName(self,name):
        self.name= name
    def setage(self,age):
        self.age= age
    def sethunger(self,hunger):
        self.hunger= hunger
    def setplayful(self,playful):
        self.playful=playful
    
    def __str__(self):
        return(self.name+' is '+str(self.age)+' years old')
        
class dog(pet):
    def __init__(self, name, age, hunger,playful,breed, favouriteToy):
        pet.__init__(self,name,age,hunger,playful)
        self.breed= breed
        self.favouriteToy= favouriteToy
    def wantstoplay(self):
        if self.playful == True:
            return('dog wants to play with '+ self.favouriteToy)
        else:
            return("dog doesn't want to play")
        
class human:
    def __init__ (self, name, pets):
        self.name= name
        self.pets= pets
    def haspets(self):
        if len(self.pets)!=0:
            return 'yes'
        else:
            return 'no'


    
        

huskeydog= dog('snowball',5, False,True,'huskey','stick')
        
play=huskeydog.wantstoplay()
print(play)
huskeydog.playful = False
play= huskeydog.wantstoplay()
print(play)


averageHuman= human('alice',[huskeydog])
haspet= averageHuman.haspets()
print(haspet)
print(averageHuman.pets[0].name)





pet1=pet('lilo',3, False, True)


    
print(pet1.getName())
print(pet1.gethunger())
pet1.setName('snowball')
print(pet1.getName())
print(pet1.name)
pet1.name='jim'
print(pet1.name)
