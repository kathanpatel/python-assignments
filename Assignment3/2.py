l1 = [x for x in range(1, 11)]
print("list l1:\n", l1)

l2 = [y for y in range(10, 100, 10)]
print("list l2:\n", l2)

l3 = ['python', 'django', 'flask', 'string', 'function', 'classes']
print("list l3:\n", l3)

main_list1 = []
main_list1.append(l1)
main_list1.append(l2)
main_list1.append(l3)
print("the complete list using append function is:\n", main_list1)

main_list2 = []
main_list2.extend(l1)
main_list2.extend(l2)
main_list2.extend(l3)
print("the complete list using extend function is:\n", main_list2)

l5 = l1 * 2
print("list l5:\n", l5)

main_list1.append(l5)
print("new main list is:\n", main_list1)

a = main_list1.count(1)
print("the occurence of the integer 1 in the list is:", a)
