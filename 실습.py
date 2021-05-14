sentence1 = "never odd or even."

str = ''
# for x in sentence1:
#     print(x)

for x in sentence1:
    if x != '.' and x != ' ':
        str += x

print(str)