import modul


#regular function
# def function (*args):
#     result = sum(args)

#     return result

# print (function(1,2,3))


#Anonymous Function using Lambda Expression
function = lambda *args : sum(args)

print (function(1,2,3))


#Modul import function
penjumlahan2 = modul.penjumlahan(2,3)
print(penjumlahan2)

