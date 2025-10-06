z=1
while(z==1):
    print("\n1> occurence of a word")
    print("2> character frequency of a word")
    print("3> factors of number")
    print("4> Exit")
    n=int (input("enter choice: "))
    if n==1:
        text=str(input("enter a sentence: "))
        word=text.split()
        s=set(word)
        for i in s:
            print(i, "= ",word.count(i))
    elif n==2:
        text=str(input("enter a word: "))
        s=set(text)
        for i in s:
            print(i, "= ",text.count(i))
    elif n==3:
        f=int (input("enter number: "))
        fact=1
        for i in range(1,f+1):
            fact*= i
        print("factorial: ",fact)
    elif n==4:
        break;
