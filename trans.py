import csv
import dic

csv_data = csv.reader(open('data.csv', encoding='utf-8'))

w_data = []
n_data = []

for data in csv_data:
    w_data.append(data[0])
    n_data.append(data[1])

csv_write = csv.writer(open('word_trans.csv', 'w', newline = '', encoding='utf-8'))

for i in range(len(w_data)):
    if int(n_data[i]) > 1:
        l = []
        try:
            cn = dic.trans(w_data[i])
            l = [n_data[i], w_data[i], cn]
            csv_write.writerow(l)
        except KeyboardInterrupt:
            print('【退出】')
            break
        except:
            print('【未知的错误】')
            csv_write.writerow([n_data[i], w_data[i], '【失败】'])

        print(l)
