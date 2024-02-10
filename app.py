#Data Type

firstName = "Argi" 
age = 20
nim = 3.99
isGraduate = True
score = {"Math":100, "Physic":100, "Biology":100} #dictionary
programId =[1,"Machine Learning", True, 22.05] #list
programId2 = (1,"Machine Learning", True, 22.05) #tuple
index1 = {1,2,3,4,5,6,7} #set
index2 = {4,7,8,9} #set

programId[0] = 2 #list index replacement . note : it can't br done in tuple

score['chemical'] = 100 #add data to dictionary
del score['Biology'] #delete data in dictionary
score ["Physic"] = 99 #replace data in dictionary

print("=====================================")
#String in Python
print(("my name is %s"%(firstName))) #string concatination
print(firstName[2]) #index access
print(firstName[2:]) #slicing

print("=====================================")
#List manipulation
print(programId)
print(programId[1:4]) #sequence(x[start:stop:step])
print(programId[0]) #Index access in list

print("=====================================")
#Tuple manipulation
print (programId2[1:4]) #sequence(x[start:stop:step])

print("=====================================")
#set manipulation. note: set doesn't have index
print(index1.union(index2))
print (index1.intersection(index2))

print("=====================================")
#dictionary manipulation
print(score)

print("=====================================")
#data conversion
print (float(age))
print(tuple(score))
print(str(age))

