Amount = int(input("Please enter amount for withdrawal:"))
note1 = Amount//100
note2 = (Amount%100)//50 
note3 = ((Amount%100)%50)//10

print ("Amount of 100 rupees:", note1)
print ("Amount of 50 rupees:", note2)
print ("Amount of 10 rupees:", note3)