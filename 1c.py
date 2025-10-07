num = int(input("Enter the number of tuples: "))
tup_list = []
for i in range(num):
    elements = input(f"Enter elements of tuple {i+1} separated by spaces: ")
    tuple_elements = tuple(map(int, elements.split()))
    tup_list.append(tuple_elements)
result = list(map(sum, tup_list))
print("Sum of elements in each tuple:", result)

​
​
