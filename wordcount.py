from sys import argv

def check_count(w, wordcount):
    w = w.strip('",.!:;-?_()').lower()
    if wordcount.get(w):
        wordcount[w] += 1
    else:
        wordcount[w] = 1
    return wordcount

def sort_list(wordcount):
    sorted_list = [i for i in wordcount.iteritems()]

    sorted_list.sort(key=lambda i: i[0])
    sorted_list.reverse()
    sorted_list.sort(key=lambda i: i[1])
    sorted_list.reverse()

    return sorted_list

def main():
    script, filename = argv

    text = open(filename)

    wordcount = {}

    for line in text:
        words = line.strip('\n').split(" ")
        for word in words:
            if word.isalpha():
                wordcount = check_count(word, wordcount)
            else:
                for letter in word.lower():
                    if not letter.isalpha():
                        clean_word = word.split(letter)
                        for c in clean_word:
                            if c != "":
                                wordcount = check_count(c, wordcount)
                        break

    sorted_list = sort_list(wordcount)

    for item in sorted_list:
        print item[0], item[1]

if __name__ == "__main__":
    main()


