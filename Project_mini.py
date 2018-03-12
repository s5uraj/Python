#A program asks user to enter file name and scrambles each word of it having length more than 3 except punctation symbols.
import random
new_list=[]
def rec(my_list):
    if not my_list:
        return new_list 
    else:
        ran=random.randint(0,len(my_list)-1)
        new_list.append(my_list.pop(ran))
        rec(my_list)
    return new_list

file=input("Enter File name")
fd=open(file,'r')
var=fd.read()
#var="suraj nad. howww . aree yu"
for x in var.split():
    if len(x) > 3:
        new_list=[]
        if x.find(".") ==-1:
            my_list = [i for i in x]
            sc = ''.join(rec(my_list))
        else:
            x = x.replace(".", "")
            my_list = [i for i in x]
            sc = ''.join(rec(my_list))
            print(sc)
            sc=sc.join('.')
    else:
        sc=''.join(x)
    print(sc)

    







