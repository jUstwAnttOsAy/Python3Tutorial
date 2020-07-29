import sys 
file = open(sys.argv[1], 'w') #參數要改成w
file.write('test') #寫入test, 會覆蓋目前文件的內容
file.close()