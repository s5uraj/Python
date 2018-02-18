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

 
word="Suraj"
my_list = [i for i in word]
sc = ''.join(rec(my_list))
print(sc)

