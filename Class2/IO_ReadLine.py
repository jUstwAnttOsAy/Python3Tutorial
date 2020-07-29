import sys
file = open(sys.argv[1], 'r', encoding='UTF-8') #要加上encoding!!!
while True:
    #下面程式碼使用WHILE迴圈, Python的縮行要統一
    line = file.readline() #一行一行進行讀取, 若無資料line=''
    if not line:break #判斷文件讀取完成
    print(line, end='') #print預設會換行, 若加上end='', 則會在每次print後面加上''
file.close()