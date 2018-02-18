#A program asks user to enter file name and scrambles each word of it having length more than 3 except punctation symbols.
import random
file=input("Enter File name")
fd=open(file,'r')
word=fd.read()
fd=open(file,'r')
my_list = [i for i in word]
def idword(word):
    count=0
    for line in word:
      print("0")  

idword(fd)
print(my_list)


