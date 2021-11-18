rating = float(input("Enter number: "))
my_list = [9,8,8,7,6,5,5,4,3,2,2,1]
count_ = my_list.count(rating)
for element in my_list:
    if count_ > 0:
        i = my_list.index(rating)
        my_list.insert(i+count_, rating)
        break
    else:
        if rating > element:
            count_ = my_list.index(element)
            my_list.insert(count_, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print(my_list)

