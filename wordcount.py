from sys import argv

script, filename = argv

text = open(filename)

wordcount = {}

for line in text:
    line = line.split(" ")
    for l in line:
        if wordcount.get(l):
            wordcount[l] += 1
        else:
            wordcount[l] = 1

for k, v in wordcount.iteritems():
    print k, v

