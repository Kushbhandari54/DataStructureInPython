arr=[7, 1, 2, 3, 4, 5, 6]
lst=[]

arr.sort(reverse=True)
i=0
j=len(arr)-1
while(i<j):
    lst.append(arr[i])
    i+=1
    lst.append(arr[j])
    j-=1

print(lst)
