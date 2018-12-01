lucky_numbers = [1,3,5,7]
friends = ["kevin","karen","jim","oscar"]

#friends.extend(lucky_numbers)#add two lists together
#print(friends)#['kevin', 'karen', 'jim', 'oscar', 1, 3, 5, 7]

friends.append("kylie")
print(friends)#['kevin', 'karen', 'jim', 'oscar', 1, 3, 5, 7, 'kylie']

friends.insert(1,"kelly")
print(friends)#在1的位置插入Kelly，其余向后移动
#['kevin', 'kelly', 'karen', 'jim', 'oscar', 1, 3, 5, 7, 'kylie']

friends.remove("kylie")
print(friends)#移除字符串kylie

friends.pop()
print(friends)#移除列表里最后一个字符

print(friends.index("kevin"))#找位置
print(friends.count("jim"))#计数

friends.sort()#按序打印列表
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)#倒序打印列表内容
#friends.clear()#清空列表
#print(friends)#[]

friends2 = friends.copy()
print(friends2)#复制