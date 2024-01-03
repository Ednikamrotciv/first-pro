participantNumber=5
participantData=[]
registeredparticipant=0
outputFile= open('participantData.txt','w')
while(registeredparticipant<participantNumber):
    temppartdata=[] #name, countrty,age
    name= (input('write your name here: '))
    temppartdata.append(name)
    age= int(input('write your age here: '))
    temppartdata.append(age)
    country= input('write your country here : ')
    temppartdata.append(country)
    participantData.append(temppartdata)
    print(participantData)
    registeredparticipant+=1
for part in participantData:
    for data in part:
        outputFile.write(str(data)) #25='25'
        outputFile.write(' ')
    outputFile.write('\n')
outputFile.close()

inputFile=open('participantData.txt','r')
inputList=[]
for line in inputFile:
    tempParticipant=line.strip('\n').split()
    # print(tempParticipant)
    inputList.append(tempParticipant)
    # print(inputList)
age={}
for part in inputList:
    tempage= int(part[-1])
    if tempage in age:
        age[tempage]+=1
    else:
        age[tempage]=1
print(age)


inputFile.close()