with open('1.txt', encoding='utf-8') as f:
    file_name = '1.txt'
    qty_lines = 0
    text = []
    dict_1 = dict()
    for line in f:
        #line = line.replace("\n", "")
        text.append(line)
        qty_lines += 1
    dict_1[qty_lines] = [file_name] + [text]

with open('2.txt', encoding='utf-8') as f:
    file_name = '2.txt'
    qty_lines = 0
    text = []
    dict_2 = dict()
    for line in f:
        #line = line.replace("\n", "")
        text.append(line)
        qty_lines += 1
    dict_2[qty_lines] = [file_name] + [text]

with open('3.txt', encoding='utf-8') as f:
    file_name = '3.txt'
    qty_lines = 0
    text = []
    dict_3 = dict()
    for line in f:
        #line = line.replace("\n", "")
        text.append(line)
        qty_lines += 1
    dict_3[qty_lines] = [file_name] + [text]

all_text = dict()
all_text.update(dict_1)
all_text.update(dict_2)
all_text.update(dict_3)

all_text = dict(sorted(all_text.items()))

box_text = []

box_text.append(list(all_text.items()))

with open ('4.txt', 'w', encoding='utf-8') as f:
    for count_1 in box_text:
        for count_2 in count_1:
            f.write(f'{count_2[1][0]}\n')
            f.write(f'{str(count_2[0])}\n')
            f.write(f'{"".join(count_2[1][1])}\n')
