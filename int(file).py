# file=open('filename','r') #r,w,r+
# file.close()
cities=['london','paris','newyork','utah']
citiesFile=open('citiesPlaces','w') #citiesPlaces creates a directory to write
for places in cities:
    citiesFile.write(places+'\n')
# print('done')
citiesFile.close()
citiesFile=open('citiesPlaces','r')
Firstline=citiesFile.readline()
print(Firstline)
secline=citiesFile.readline()
print(secline)
# AllFile=citiesFile.read()
# print(AllFile)
for line in citiesFile:
    print(line, end='')
citiesFile.close()
finalspot='nigeria'
citiesFile=open('citiesPlaces','a')
citiesFile.write(finalspot)
citiesFile.close()
with open('citiesplaces','r') as citiesFile:#you dont need the .close
    for line in citiesFile:
        print(line, end='')
