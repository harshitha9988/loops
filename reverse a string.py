string=input("please enter your own string:  ")

string2=('')

for i in string:
    string2=i+string2

print("\nThe original String +",string)
print("the reversed String=",string2)