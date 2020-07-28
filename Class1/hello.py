filename = input("檔名:") #使用者輸入檔名

file = open(filename, 'r', encoding='UTF-8') #讀取檔案
content = file.read() #讀取內容寫入暫存
file.close() #關閉讀取流

print(content) #哈囉!世界!
print(content.encode('UTF-8')) #'\xe5\x93\x88\xe5\x9b\x89!\xe4\xb8\x96\xe7\x95\x8c!'
print(content.encode('UTF-8').decode('UTF-8')) #哈囉!世界!