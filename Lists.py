list1=[20,"shiva","gk"]
# for i in list1:
#     print(i)
list1[0]=21
for i in list1:
    print(i)
list1[2]=41
for i in list1:
    print(i)
list1.append("ravi")
print(list1)
list2=["xxx",41]
list1.extend(list2)
print(list1) 
list1.insert(3,"s")
print(list1)
list1.insert(4,"p")
print(list1)
print(len(list1))
list1.append('abc')
print(list1)

list1.append('prashant')

print(list1)
list1.remove('shiva')
print(list1)
 
print("len of list1",list1[len(list1)-1]) 

s = '{}'
i = 0
while  i < len(s):
    print("s of i",s[i])
    i += 1
    # print(list1.pop())
    
print('list is empty')
 
           