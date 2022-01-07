#Given a sorted and rotated array, find if there is a pair with a given sum

from seachInRotatedarr import rotateArr

if __name__=='__main__':
    lst=[11, 15, 26, 38, 9, 10]
    x=45
    temp=-1
    for i in range(1,len(lst)):
        if lst[i-1]>lst[i]:
            temp=i
    a=rotateArr(lst,temp)
    f=0
    l=len(a)-1
    while(f<l):
        if a[f]+a[l]==x:
            print("Founded")
            break
        elif a[f]+a[l]>x:
            l-=1
        else:
            f+=1
    else:
        print("Not Founded")