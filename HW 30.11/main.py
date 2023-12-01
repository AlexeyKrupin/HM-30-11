files = ['1.txt', '2.txt', '3.txt']

file_contents = []
for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_contents.append((file_name, len(lines), lines))

file_contents.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_info in file_contents:
        result_file.write(file_info[0] + '\n')
        result_file.write(str(file_info[1]) + '\n')
        result_file.writelines(file_info[2])
        result_file.writelines('\n')