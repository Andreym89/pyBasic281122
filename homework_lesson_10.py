# Files
'''
with open('files/testFile.txt', 'wt') as file: # 'at' - добавить к концу файла еще данные если будут
    for i in range(0, 4):
        file.write('Hello world\n')

li = ['123', 'qwe', '456']

with open('files/testFile.txt', 'at') as file:
    file.writelines([i+'\n' for i in li])


with open('files/testFile.txt', 'rt') as file:
    result = file.read()
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.read(14)
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.readline()
    print(result)


with open('files/testFile.txt', 'rt') as file:
    result = file.readlines()
    print(result)

'''


def read_txt_file(filename: str):
    with open(filename, 'rt') as file:
        data = file.read()
        return data
    return 0


def write_txt_file(filename: str, data) -> None:
    with open(filename, 'wt') as file:
        data = file.write(str(data))


text = read_txt_file('files/testFile.txt')
if text != 0:
    print(text)