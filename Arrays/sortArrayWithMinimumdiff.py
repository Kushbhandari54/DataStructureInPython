x = 7
arr = [10, 5, 3, 9, 2]
dict={}
lst=[]

for i in range(len(arr)):
    dict[arr[i]]=abs(arr[i]-x)


m={k:v for k,v in sorted(dict.items(),key=lambda dict:dict[1])}

for i in m.keys():
    lst.append(i)
print(lst)