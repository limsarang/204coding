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