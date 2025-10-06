total=0
list1=[25,1,3,4,7,30]
list2=[15,16,39]
for i in list1:
    total+=i
c=0
for j in list2:
    c+=j
if total==c:
    print("the sum of two list are same",total,"=",c)
else:
    print("the sum of two list are different",total,"=",c)
