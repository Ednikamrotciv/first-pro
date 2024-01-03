from random import shuffle
def createdeck():
    Deck=[]
    faceValues=['A','J','Q','R']
    for i in range(4):#there are 4 diff suits
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    return Deck

cardDeck=createdeck()
shuffle(cardDeck)
print(cardDeck)