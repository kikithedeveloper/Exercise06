from sys import argv

script, filename = argv

text = open(filename)

wordcount = {}

for line in text:
    words = line.strip('\n').split(" ")
    for w in words:
        w = w.strip('",.!:;-?_').lower()
        if "-" in w:
            clean_word = w.split("-")
            for c in clean_word:
                c = c.strip('",.!:;-?_')
                if wordcount.get(c):
                    wordcount[c] += 1
                else:
                    wordcount[c] = 1
        elif wordcount.get(w):
            wordcount[w] += 1
        else:
            wordcount[w] = 1

sorted_list = [i for i in wordcount.iteritems()]

sorted_list.sort(key=lambda i: i[0])
sorted_list.reverse()
sorted_list.sort(key=lambda i: i[1])
sorted_list.reverse()

for item in sorted_list:
    print item[0], item[1]


