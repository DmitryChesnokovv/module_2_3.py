my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_list = []
index = 0
while index < len(my_list):
    num = my_list[index]

    if num > 0:
        positive_list.append(num)
    elif num == 0:
        index += 1
        continue
    else:
        break

    index += 1
for num in positive_list:
    print(num)
