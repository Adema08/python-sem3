# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

a = [1, 1, 2, 0, -1, 3, 4, 4]
new = []
for i in a:
    if i not in new:
        new.append(i)
print(len(new))

# for i in a:
#     for j in new:
#         if a[i] == new[j]:
#             break
#     else:
#         new.append[a[i]]
# print(len(a))

# Через срезы
# arr = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0
# for i in range(len(arr)):
# if (arr[i]) not in arr[:i]:
# count += 1
# print(count)

# Через множество
# arr = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(arr)))