#Conditional "For"

var_list =[1,2,3,4,5,6,7,8,9,10]

for i in var_list:
    print (i)

    
print("======================")
#range (start, stop, steps)

for i in range (1, 11, 1): #step default value is 1
    print(i)

print("======================")
#Conditional "While"
    
counter = 1

while counter < 5:
    print(counter)
    counter +=1

print("======================")
#Nested "For"
    
for i in range(1,3):
    for j in range (1,3):
        print (i,j)
    

print("======================")
#Iteration Control

for i in range(2):
    print("Perulangan luar:", i)
    for j in range(10):
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

print("======================")
#Stop until fnding the True condition
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

print("======================")
#Continue until fnding the True condition
for huruf in 'Dico ding':
    if huruf == ' ': #just pass the condition and continue everything
        continue
    print('Huruf saat ini: {}'.format(huruf))

print("======================")
#Else for in Iteration
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

print("======================")
#Else after While
count = 1
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

print("======================")
#Pass
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

print("======================")
#List Comprehension

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

print("======================")
#List Comprehension without append
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)