# Task 1
def read_line(n=None, file=None):
    try:
        if type(n) != type(int()) or type(file) != type(str()):
            return "invalid input detected"
        text = open(file, 'r')
        lines = []
        for line in text:
            lines.append(line)
        line_num = n-1
        length = len(lines)
        if line_num > length:
            return f"Line {n} doesn't exist"
        elif lines[n-1] == ' \n':
            return f'" "'
        else:
            return lines[n-1]
    except:
        return "file not found"


# print(read_line(4.0, "ex3_text.txt"))


# Task 2
def longest_words(file=None):
    try:
        word_len = dict()
        lines = []
        words_list = []
        text = open(file, 'r')
        for line in text:
            line = line.rstrip('\n,-[]"". ')
            lines.append(line)
        length1 = len(lines)
        for words in range(length1):
           words_list.append(lines[words].split())
        for word in words_list:
            for keys in word:
                word_len[keys] = len(keys)
        return sorted(word_len, key=word_len.get, reverse=True)[:5]
    except:
        return f"file not found\n{words_list}"


# print(longest_words("ex4_text.txt"))



