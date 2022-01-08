#Program for array rotation
arr=[1,3,4,5,6,7]
n=int(input("Enter the no. of times the array needed to rotate"))

print("The array before rotation is {}".format(arr))
n=n%len(arr)

print(arr[n:]+arr[:n])
# while(n>0):
#     a=arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1]=arr[i]
#     arr[-1]=a
#     n-=1

# print("The array after rotation is {}".format(arr))

