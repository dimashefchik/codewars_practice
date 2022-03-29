ls = [1, 2, 3, 4, 5, 6]

# result = []
# i = 0
# while i <= len(ls):
#     result.append(sum(ls[i:]))
#     i += 1
# print(result)


sums = [sum(ls)]
for i in ls:
    sums.append(sums[-1]-i)
print(sums)