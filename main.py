import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter3=chr(random.randint(97,122))
lowercaseLetter4=chr(random.randint(97,122))
number1=chr(random.randint(48,57))
number2=chr(random.randint(48,57))
specialchar1=chr(random.randint(33,47))
specialchar2=chr(random.randint(33,47))
#Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + number1 + number2 + specialchar1 + specialchar2;
password = shuffle(password)

#Ouput
print(password)