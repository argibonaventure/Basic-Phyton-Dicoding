#Conditional in reguler syntax

nilai = 80
perilaku = "baik"


if nilai >= 80 and perilaku == "baik":
    print ("you've passed the test")
    print ("study harder, and your dream will come true !")
   
elif nilai >= 70 and perilaku == "baik":
     print("You are really good")
     print("improve your study skill!")
else : 
    nilai >= 60 and perilaku == "baik"
    print("You are good")
    print("study harder !")

print("========================================")
#Conditional in Ternary Syntax
    
print ("you've passed the test test") if nilai >= 80 else print ("Study Harder !")


print("========================================")
#Conditional in Ternary Tuples

print(("Study Harder","You've passed the test")[nilai >= 80])