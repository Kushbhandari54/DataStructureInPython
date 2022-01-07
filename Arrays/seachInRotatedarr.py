#Search an element in a sorted and rotated array
def rotateArr(arr,n):
    while(n>0):
        first_element=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=first_element
        n-=1
    return arr
def binarySearch(arr,key):
    lower=0
    upper=len(arr)-1
    while(lower<=upper):
        mid=(lower+upper)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            upper=mid-1
        else:
            lower=mid+1
    return -1    

if __name__=='__main__':
    arr=[30, 40, 50, 10, 20]
    key=10
    temp=-1
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            temp=i
arr1=arr[:temp]
arr2=arr[temp:]

a=binarySearch(arr1,key)
b=binarySearch(arr2,key)
if a==-1 and b==-1:
    print(-1)
elif a==-1:    
    print(len(arr1)+b)
elif b==-1:
    print(a)

#arr=rotateArr(arr,temp)
#print(arr)
#print(binarySearch(arr,key))






