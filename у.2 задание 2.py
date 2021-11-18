my_str = input('Number:')
my_list = my_str.split()
print(my_list)

n = len(my_list)
if n % 2 != 0:
    n = n - 1
print(n)

for i in range(0, n, 2):
    y = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = y

print(my_list)