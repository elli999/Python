# -*- coding:utf-8 -*-

# 需求：读取文件中的2、6、10、14... 行内容并写入新文件
# 下面是方法一

input_file = open(r"./text1/source.srt", 'r', encoding='utf-8')
output_file = open(r"./text1/EK_out.txt", 'w', encoding='utf-8')

line_list = input_file.readlines()

# output_text 为测试变量，只在程序内的结果输出
output_text = ''

n = 1

while True:
    i = 4 * n - 2
    if i <= len(line_list):
        output_text += line_list[i]
        output_file.write(line_list[i])
    else:
        break
    n += 1


print(output_text)

# 看看列表中有多少个element
print(len(line_list))

input_file.close()
output_file.close()
