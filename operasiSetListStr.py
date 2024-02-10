#Len (to count the data length)
thisList = [1,2,3,4,5,6,7]
toSet = set(thisList)

print(len(thisList))
print(len(toSet))

print("=====================================")
#Min & Max
number1 = (1,3,5,45,13,56,5,7,11)
number2 = [3,5,7,12,3,12,77,90,1,12,3,4]

print(max(number1))
print(min(number2))

print("=====================================")
#Count (to count the number of particular value)
string1 = "aku adalah anak gembala selalu riang serta gembira"

print(number1.count(5))
print(number2.count(12))

print(string1.count('a'))


print("=====================================")
#In or Not in

print('gembala' in string1)
print('soleh' in string1)
print('aku' not in string1)


print("=====================================")
#Save in new Variable
string2 = ['Argi', 'Informatics Technology', 4, 2021]

name, major, semester, year = string2

print(string2)
print(name)
print(major)
print(semester)
print(year)


print("=====================================")
#Sort Ascending and Descending for List
string3 = ['apple', 'manggo', 'guava', 'pear']
string4 = ['apple', 'Manggo', 'guava', 'pear']

string3.sort()

print(string3)

string3.sort(reverse=True)

print(string3)

string4.sort(key=str.lower) #transform to lowercase first to sort correctly

print(string4)