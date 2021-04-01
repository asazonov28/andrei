same_word = input('Please enter the word: \n-> ')
file = open('C:/Users/asazo/PycharmProjects/pythonProject/Student//trimushketera.txt', 'r', encoding='utf8')
with open('C:/Users/asazo/PycharmProjects/pythonProject/Student//trimushketera.txt', 'r', encoding='utf8') as read_file:
    file = read_file.read()
    file = file.replace(",", "").replace(":", "").replace("!", "").replace("?", "").replace(";", "").replace(".", "")
    word = len(file)
    count_word = file.count(same_word)
    print(count_word)