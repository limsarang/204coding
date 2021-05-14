# counter = [0, 2, 3, 5]
#
# def 최대값(arr):
#     가왕 = 0
#     for x in arr:
#         if x > large:
#             large = x
#     return large
# 최대값(arr)

#----------------------------------
#4
def solution(arr):
    left = 0
    right = len(arr) - 1

    while (left < len(arr)/2):
        #arr[left]과 arr[right]의 값을 서로 바꿈
        # temp = arr[left]
        # arr[left] = arr[right]
        # arr[right] = temp

        arr[left], arr[right] = arr[right], arr[left]   #위의 코드와 같음

        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("Solution: return value of the function is ", ret, " .")

#----------------------------------
#6
def solution(scores):
   count = 0
   for s in scores:
       # if 650 <= scores[s] and scores[s] < 800:
       if 650 <= s < 800:       #파이썬 문법만 해당
           count += 1
   return count

#The following is code to output testcase. The code below is correct and you shall correct solution function.
scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")