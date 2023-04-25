expressions = input().split('-')
for i in range(len(expressions)):
    nums = expressions[i].split('+')
    expressions[i] = sum(list(map(int, nums)))

print(eval('-'.join(list(map(str, expressions)))))