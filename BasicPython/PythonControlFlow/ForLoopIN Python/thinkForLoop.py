# for loop in python loop is iterating through some number something

# studentHeight = [180, 124, 165, 173, 189, 169, 146]
# studentHeight = input("enter a list of student height using comma ").split(',')
#
# for n in range(0, len(studentHeight)):
#     studentHeight[n] = int(studentHeight[n])
# # print(studentHeight)
# # print(len(studentHeight))
# # print(sum(studentHeight))
# # print(round(sum(studentHeight)/len(studentHeight)))
# count = 0
# add = 0
# for i in studentHeight:
#     print(i)
#     add = add + int(i)
#     count = count + 1
# averageHeight = round(add / count)
# print(f'the average of the height  {averageHeight}')

# example2 Student score
exampleList = [78, 65, 89, 86, 55, 91, 64, 89]
studentScore = input('Enter the score of the student using comma: ').split(',')

for n in range(0, len(studentScore)):
    studentScore[n] = int(studentScore[n])
# print(studentScore)

highestScore = 0
for i in studentScore:
    print(i)
    if highestScore <= i:
        highestScore = i
print(f'the highest Score of the class is {highestScore}')

# studentScore = input('Enter the score of the student using comma: ').split(',')
#
# for n in range(0, len(studentScore)):
#     studentScore[n] = str(studentScore[n])
# print(studentScore[0])
