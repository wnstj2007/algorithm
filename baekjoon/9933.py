n = int(input())
word = []
for i in range(n):
    word.append(input())
for i in word:
    tmp = i[::-1]
    if tmp in word:
        password = i
        break
print('{} {}'.format(len(password), password[len(password)//2]))