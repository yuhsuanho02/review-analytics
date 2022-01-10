commont = []
count = 0
with open('reviews.txt', 'r') as rvw:
    for cmt in rvw:
        commont.append(cmt)
        count += 1
        if count % 10000 == 0:
            print(len(commont))
print(len(commont))
print(commont[0])
print('-------------------------------')
print(commont[1])