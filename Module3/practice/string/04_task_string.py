# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here
t=0
word_len=0
while t < len(text):
    if text[t] ==" ":
        print(word_len)
        word_len = 0
    else:
        word_len += 1
    t += 1
print(num_long_word)
