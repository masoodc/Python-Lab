mark1=int(input("enter First mark: "))
mark2=int(input("enter Second mark: "))
mark3=int(input("enter Third mark: "))
if mark1>mark2:
    if mark1>mark3:
        print(mark1 ," is greater than" ,mark2 ,"and",mark3)
    else :
        print( mark3 ," is greater than" ,mark2 ,"and",mark1)
else :
    print( mark2 ," is greater than" ,mark3 ,"and",mark1)
