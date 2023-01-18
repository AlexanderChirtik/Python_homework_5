# 4. Реализуйте RLE алгоритм

with open('file.txt', 'w') as data:
    data.write('weyfg7632gr2g3riu278g')
with open('file.txt', 'r') as data:
    text = data.readline()
with open('file_exit.txt', 'w') as data:
    data.write('')
count = 1
for i in range(len(text)-1):
    if i <= len(text):
        if text[i] == text[i + 1]:
            count += 1
        else:
            with open('file_exit.txt', 'a') as data:
                data.write(f'{count }, {text[i]}')
            count = 1

