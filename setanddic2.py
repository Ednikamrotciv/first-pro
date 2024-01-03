blackShoes={42:2,41:3,40:4,39:1,38:0}
print(blackShoes)
while(True): #true==true- comparison is going on
    purchaseSize=int(input('which shoe size would you like to buy?\n'))# \n means newline for good formaTTING
    if blackShoes[purchaseSize]>0:
        blackShoes[purchaseSize]-=1 #blackShoes[purchaseSize]-1
    else:
        print('no shoes')
    print(blackShoes)