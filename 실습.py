# 숫자를 입력하고 입력받은 숫자가
# 몇 번 박수를 치는지 알아보자

# 방법 1 : 대부분의 사람들이 생각하는 방법
a = 33
문자 = str(a)

count = 0
for x in 문자:
    if x == '3' or x == '6' or x == 9:
        # 카운트를 증가
        count += 1
print(count)