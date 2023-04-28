string = input("Enter a string: ")
list=[]
string = string.lower()
for i in string:
    list.append(i)
final_list=set(list)
for i in  final_list:
    print(i,end=",")