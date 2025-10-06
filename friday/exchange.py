word= str(input("enter the word : "))
x=len(word)
f_letter=word[0]
l_letter=word[x-1]
result = l_letter +word[1:x-1]+f_letter
print(result)
