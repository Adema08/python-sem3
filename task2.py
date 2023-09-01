# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [3, 4, 5, 1, 2]

my_list = [1, 2, 3, 4, 5]
k = int(input('-> '))
k %= len(my_list)
for _ in range(k):
    last_item = my_list.pop()
    my_list.insert(0, last_item)
print(my_list)

# Через срезы
# -5 -4 -3 -2 -1
# 0 1 2 3 4
# my_list = [1, 2, 3, 4, 5]
# # 3, 4, 5, 1, 2
# # 4, 5, 1, 2, 3
# k = int(input('-> '))
# k %= len(my_list)
# print(my_list[-k:] + my_list[:-k])
## print(my_list[k-1:] + my_list[:k-1])