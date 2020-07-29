import sys #載入sys模組
file=open(sys.argv[1], 'r', encoding = 'UTF-8') 
#sys.argv為list, 儲存命令列引數, sys.argv[0]固定為模組名稱, ex. python3.5 hello.py one two three, 分別於sys.argv對應0,1,2,3對索引
#如果文件為包含中文, 一定要指定encodeing='UTF-8', 不然會發生錯誤
content = file.read() #使用read讀取檔案
file.close() #讀取完成時一定要關閉
print(content)