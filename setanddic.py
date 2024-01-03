# sets={'age1', 'age2', 'age1', 'age 4'}
# print(sets)
# if 'age2' in sets:
#     print('yes')
countryList=[]
for i in range(5):
    country= input('please enter your country:')
    countryList.append(country)
countrySet= set(countryList)

# print(countryList)
# print(countrySet)

# if 'lome' in countrySet:
#     print('attended')

# dictionary={'key':'value','key2':'value2','key3':'value3'}

countryDictionary= {}
for country in countryList:
    if country in countryDictionary:
        countryDictionary[country] +=1
    else:
        countryDictionary[country]=1
print(countryDictionary)
