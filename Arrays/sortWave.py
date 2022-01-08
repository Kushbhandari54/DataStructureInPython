#Sort an array in wave form
arr=[10, 5, 6, 3, 2, 20, 100, 80]

arr.sort()
#arr=[2,3,5,6,10,20,80,100]

lst1=[]
i=0
j=len(arr)-1
while(i<j):
    lst1.append(arr[i])
    lst1.append(arr[j])
    i+=1
    j-=1
    
print(lst1)
