#this a password genrator application. We will use RANDOM and STRING.
#password consist of lower case, upper case, number , symbols
import random
import string

print(" yay lets create a passoword")
#we define how long the password is going to be (always bigger than 8)
long = int(input(f'how long you want it: '))

#data value
low = string.ascii_lowercase
up = string.ascii_uppercase
num = string.digits
sym = string.punctuation
#now we need to combine all 
all = low + up + num + sym
#now we use random to genrate the password
gen = random.sample(all,long)
#this is where the pasword is genrated
password = "".join(gen)
#now we print the password
print(password)
