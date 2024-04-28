
# # List Comprehension
# # New_list=[New_item(what just do the new item
# # ) for item in list]
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)
# # conditional list Comprehension
# # new_list=[new_item for item in list if test]


# C1


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers=[i**2 for i in numbers]
# print(squared_numbers)
# C2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [i for i in numbers if i % 2 == 0]
# print(result)
# C3
with open("file1.txt") as file1:
    file11 = file1.readlines()
with open("file2.txt") as file2:
    file22 = file2.readlines()
# for i in file22, file11:
#     # print(i)
#     if i in file22 == i in file11:
#         i=i.strip()
#         print(i.strip())

result=[int(num) for num in file11 if num in file22]
print(result)