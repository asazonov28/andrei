# работа с файлами

# 'r' - read
# 'a' - apend
# 'w' - write
# 'x' - create
# 'r+' - read and write


# file = open('text.txt', 'r', encoding='utf8')
# print(file.name)
# print(file.closed)
# while True:
#     continue
# print(file.closed)
# file.close()
# print(file.closed)

# with open('text_copy.txt', 'r+', encoding='utf8') as file:
#     print(file2.name)
#     print(file2.closed)
#
# print(file2.closed)
#     file_content = file.read()
#     print(file_content)
#     print(type(file_content))
#     file_content = file.readlines()
#     file_content = file.readline()
#     print(type(file_content))
#     print(len(file_content))
#     print(file_content)
#
#     file_content = file.readline()
#     print(file_content)
# for line in file_content:
#     print(line)

    # file_content = file.read()
    # print(file_content, end='n\n\n\t')
    # print('Hello world')

    # size_to_read = 1000
    # file_content = file.read(size_to_read)
    # while len(file_content) != 0:
    #     print(file_content)
    #     print(len(file_content))
    #     file_content = file.read(size_to_read)

    # file_content = file.readline()
    # print(file_content)
    # # file.seek(0)
    # file_content = file.readline()
    # print(file_content)
    # data = file.read()
    # print(data)
    # file.write('TEST')
    # file.seek(0)
    # file.write('****')


# with open('text.txt', 'r', encoding='utf8') as read_file:
#     with open('text_copy.txt', 'w', encoding='utf8') as write_file:
#         for line in read_file:
#             write_file.write(line)
with open('random.jpg', 'rb') as read_file:
    with open('random.jpg', 'wb') as write_file:
        chunk_size = 4896
        data = read_file.read(chunk_size)
        while len(data) > 0:
            write_file.write(data)
            data = read_file.read(chunk_size)