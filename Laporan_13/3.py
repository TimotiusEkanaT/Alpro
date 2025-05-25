fhandle = open("mbox-short.txt")
counts = dict()
for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        if len(words) > 5:
            time = words[5]
            hour = time.split(':')[0]
            counts[hour] = counts.get(hour, 0) + 1

for hour in sorted(counts):
    print(hour, counts[hour])