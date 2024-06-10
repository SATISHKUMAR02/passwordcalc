import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nrc= int(input("How many letters would you like in your password?\n")) 
nrs = int(input(f"How many symbols would you like?\n"))
nrn = int(input(f"How many numbers would you like?\n"))

password=""
passli=[]
for i in range(1,nrc+1):
    #passli.append(random.choice(letters))
    passli+=random.choice(letters)

for i in range(1,nrs+1):
    #passli.append(random.choice(symbols))
    passli+=random.choice(symbols)
    
for i in range(1,nrn+1):
    #passli.append(random.choice(numbers))
    passli+=random.choice(numbers)

print(passli)
random.shuffle(passli)

password=""
for i in passli:
    password+=i

print(f"your password is: {password}") 

