commont = []
count = 0
with open('reviews.txt', 'r') as rvw:
    for cmt in rvw:
        commont.append(cmt)
        #count += 1
        #if count % 10000 == 0:
            #print(len(commont))
print('檔案讀取完了, 總共有', len(commont), '筆資料')
sum_len = 0
for d in commont:
    sum_len = sum_len+len(d)
print(sum_len)
print('留言的平均長度為', sum_len/len(commont))

new = [] #長度小於100的清單
for d in commont:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')



