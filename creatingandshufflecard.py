from random import shuffle
def createDeck():
    deck=[]

    faceValue=['a','j','q','k']
    for i in range(4):# there are four different suits
        for card in range(2,11): #adding numbers (2-10)
            deck.append(str(card))
        for card in faceValue:
            deck.append(card)
    shuffle(deck)
    return deck

thedeck=createDeck()
#shuffle(thedeck)
print(thedeck)

class Player:
    def __init__(self,hand=[],money=100):
        self.hand= hand
        self.score= self.setscore()
        self.money= money
        self.bet =0
    def __str__(self): #call print on (player)
        currenthand=''

        for card in self.hand:
            currenthand += str(card) + ' '
        finalstatus= currenthand + ' score: '+str(self.score)#'a 10 2 4 score:17'
        return finalstatus
    def setscore(self):
        self.score =0
        # print(self.score)
        faceCardsDict = {'a':11,'j':10,'q':10,'k':9,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
        
        acecounter=0
        for card in self.hand:
            self.score +=faceCardsDict[card]
            if card =='a':
                acecounter+=1
            if self.score > 21 and acecounter !=0:
                self.score-= 10
                acecounter-=1
        return self.score
    def hit(self,card):
        self.hand.append(card)
        self.score= self.setscore()
    def play(self,newhand):
        self.hand=newhand
        self.score=self.setscore()

    def betmoney(self,amount):
        self.money-= amount
        self.bet+= amount
    def win(self,result):
        if result==True:
            if self.score==20 and len(self.hand)==2:
                self.money+=2.5*self.bet
            else:
                self.money+= 2*self.bet
            self.bet=0
        else:
            self.bet=0
    # def lose(self,amount):
        # self.money-= amount

player1=Player(['3','7','5'])
print(player1)
player1.hit('k')
print(player1)
player1.hit('a')
print(player1)
player1.play(['a','k'])
print(player1)
player1.betmoney(20)
print(player1.money,player1.bet)
player1.win(True)
print(player1.money)
# player1.lose(30)
# print(player1.money)

def printhouse(house):
    for card in range(len(house.hand)):
        if card==0:
            print('x',end=' ')
        elif card==len(house.hand)-1:
            print(house.hand[card])
        else:
            print(house.hand[card], end = ' ')


thedeck=createDeck()
print(thedeck)
firsthand=[thedeck.pop(),thedeck.pop()]
secondhand=[thedeck.pop(),thedeck.pop()]
player1=Player(firsthand)
house=Player(secondhand)
print(player1)
printhouse(house)
while(player1.score<21):
    action= input('do you want another card?(y/n): ')
    if action=='y':
        player1.hit(thedeck.pop())
        print(player1)
        printhouse(house)
    else:
        break

print(house)