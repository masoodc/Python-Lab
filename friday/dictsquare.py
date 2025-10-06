n=int(input("enter the number of key : "))
dict1={}
if n<= 15:
    for i in range(1,n+1):
        dict1[i]=i*i
    print(dict1)
else :
    print( n,",please enter between 1 to 15 ")

