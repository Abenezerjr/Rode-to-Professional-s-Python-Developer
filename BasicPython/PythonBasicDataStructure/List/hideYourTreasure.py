row1 = ['📦', '📦', '📦']
row2 = ['📦', '📦', '📦']
row3 = ['📦', '📦', '📦']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you went to Pust yore treasure? ')  # 23
horizontal = int(position[0])  # 2
vertical = int(position[1])  # 3

selected_row = map[vertical - 1]  # 3 map=[2]
selected_row[horizontal - 1] = "X"
print(f'{row1}\n{row2}\n{row3}')
