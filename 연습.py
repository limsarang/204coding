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
    if x == 1:
        count[1] += 1
    elif x == 2:
        count[2] += 1
    elif x == 3:
        count[3] += 1

count[1] = 일
count[2] = 이
count[3] = 삼

print(f"1의 갯수 : {count[1]}")
print(f"2의 갯수 : {count[2]}")
print(f"3의 갯수 : {count[3]}")