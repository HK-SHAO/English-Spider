import csv

f = open('english.txt') # 打开txt文件
word = f.read().split(' ') # 将单词转换成列表
f.close() # 关闭txt文件

# l = [] # 统计的列表

csv_file = open('data.csv', 'w', newline = '') # 打开csv文件
csv_write = csv.writer(csv_file) # 写csv文件

while len(word) is not 0: # 当列表未空
    w = word[0] # 单词
    n = 0 # 出现的次数

    while w in word: # 当word里还有单词w
        word.remove(w) # 删除已经统计的单词
        n = n + 1 # 次数加一

    if len(w) > 3: # 过滤长度小于4的单词
        csv_write.writerow([w, n]) # 写入csv文件
        # l.append([w, n])

csv_file.close() # 关闭csv文件