"""
import random

a = random.randint(1,12)
b = random.randint(1,12)
for i in range(10):
    question = "What is "+str(a)+" x "+str(b)+"?"
    answer = int(input(question))
    if answer == a*b:
        print ("Well done!")
    else:
        print("No.")
"""

a = int(input())
b = int(input())
product = a*b
print(product)
