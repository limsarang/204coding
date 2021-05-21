list1 = [10, 20, 30, 40, 50]
for a in list1:
    a += 1  # 이렇게 하면 안됌!!

print(list1)


# list1 = [10, 20, 30, 40, 50]  #배열 1씩 추가
# for i in range(0, len(list1)):
#     list1[i] += 1
#
# print(list1)

#--------------------------------------

arr = [1,2, 3, 3, 1, 3, 3, 2, 3, 2]
count = [0, 0, 0, 0]

for x in arr:
    count[x] += 1

print(f"1의 갯수 : {count[1]}")
print(f"2의 갯수 : {count[2]}")
print(f"3의 갯수 : {count[3]}")

#--------------------------------------

sentence1 = "never odd or even."

str = ''
# for x in sentence1:
#     print(x)

for x in sentence1:
    if x != '.' and x != ' ':
        str += x

print(str)
