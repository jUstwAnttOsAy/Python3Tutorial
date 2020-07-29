import sys
for line in open(sys.argv[1], 'r', encoding='UTF-8'): #類似foreach的概念
    #記得要縮行
    print(line, end='')
#會自動關閉資料流, 不必使用close