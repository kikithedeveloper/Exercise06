open_file = open("scores.txt")

scores = {}

for line in open_file:
    items = line.split(":")
    scores[items[0]] = int(items[1])

for k, v in sorted(scores.iteritems()):
    print "Resturant '%s' is rated at %s" % (k, v)