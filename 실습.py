# 숫자를 입력하고 *1부터 입력받은 숫자가
# 몇 번 박수를 치는지 알아보자

# # 방법 1 : 대부분의 사람들이 생각하는 방법
# a = 33
# 문자 = str(a)
#
# count = 0
# for x in 문자:
#     if x in ['3', '6,' '9']:
#         # 카운트를 증가
#         count += 1
# print(count)

# 방법 2 : 컴퓨터가 생각하는 방법
a = 31
count = 0

for x in range(1, a+1):         #33을 포함하지 않기 때문에 +1
    while x:
        #if a%10 == 3 or a%10 == 6 or a%10 == 9:
        if x % 10 in [3, 6, 9]:     #일의 자리 확인(나머지)
            count += 1
        x = x // 10                 #십의 자리 확인(몫)

print(count)