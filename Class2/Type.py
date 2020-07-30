print('各類型呈現')
print(type(1)) 
#<class 'int'>
print(type(111111111111111111111111111111111111111111111))
#<class 'int'>
print(type(3.14159))
#<class 'float'>
print(type(True)) #True->T要大寫
#<class 'bool'>
print(type(3+4j))
#<class 'complex'>
print(2**100) #2的100次方
#1267650600228229401496703205376

print('數值')
print(10/3) #使用/, 結果一定會是浮點數
#3.3333333333333335
print(10/3.0)
#3.3333333333333335
print(10//3) #使用//, 整數與整數之間會產生整數, 整數與浮點數會變成浮點數
#3
print(10//3.0)
#3.0
print(1.0-0.8) #浮點數誤差同樣存在
#0.19999999999999996
#在python2中, print的結果為2, 是因為呼叫下方的函數
print((1.0-0.8).__repr__()) #repr回傳Unambiguous的字串表示
print((1.0-0.8).__str__()) #str回傳Readabled的字串表示
#但是在python3卻都產生0.19999999999999996

# 在python一樣使用decimal進行精確運算
import decimal
a = decimal.Decimal('1.0')
b = decimal.Decimal('0.8')
print(a-b)

print('字串')

# "與'可以換換
print("Juts'in") 
#Just'in
print('Juts"in')
#Just"in

#當沒有特殊字元時, 不須另外處理\
print('C:\workspace')
#C:\workspace
print('C:\\workspace')
#C:\workspace

#因為\t表Tab, 所以必須使用\\
print('C:\todo')
#C:      odo
print('C:\\todo')
#C:\todo
#或者可以在字串前加上r
print(r'C:\todo')
#C:\todo

#字串的特性為不可變(Immutable)
#此意思為記憶體位址不變
#可參考以下網址說明: https://medium.com/@oange6214/python-%E5%9F%BA%E7%A4%8E%E7%AD%86%E8%A8%98-%E5%8F%AF%E8%AE%8A%E5%8B%95%E7%9A%84-mutable-%E8%88%87%E4%B8%8D%E5%8F%AF%E8%AE%8A%E5%8B%95%E7%9A%84-immutble-54f1b7a6899
name = "Steve"
print(id(name))
#2399050405296
name = "Steve Yang"
print(id(name))
#2399050405040

#取得字串長度
print(len(name))
#10

#迭代字串
for char in name:
    print(char)
'''
S
t
e
v
e

Y
a
n
g
'''
#判斷是否存在某字串(Yang)
print('Yang' in name)
#True

#字串相加
print(name+name)
#Steve YangSteveYang

#複製字串
print(name*3)
#Steve YangSteve YangSteve Yang

#取得字串第n個字元(從0開始, 負數為從後面開始算)
print(name[0]) #第一個
print(name[-1]) #倒數第一個
'''print(name[-20]) #超過會發生錯誤'''

#[]可以切割字串
print(name[1:3]) #第2個到第3個字(不包含索引3)(所以返回的字數為3-1=2)
#te
print(name[3:]) #第4個字到結束
#ve Yang
print(name[:8]) #開始到第8個字
#Steve Ya

#[]可以指定間距
print(name[0:8:3]) #在第1個到第8個字元, 每3個取一字元
#SvY

#還可以反轉字串
print(name[::-1]) 
#gnaY evetS

#舊式寫法(不建議)
print('%d %.2f %s' % (1,99.3, 'Justin')) #%d ->數值, %.2f->小數點第2位, %s->字串
#1 99.30 Justin
print('%(real)s is %(nick)s' % {'real':'ZongHan', 'nick':'Steve'}) #類別方式
#ZongHan is Steve

#format方法(推薦)
print('{0} is {1}'.format('ZongHan','Steve'))
#ZongHan is Steve
print('{real} is {nick}'.format(real = 'ZongHan', nick = 'Steve'))
#ZongHan is Steve
print('{0}, {real} is {nick}'.format('Beeee', real = 'Zonghan', nick = 'Steve'))
#Beeee, Zonghan is Steve
import sys
print('My platform is {pc.platform}'.format(pc = sys)) #直接把物件觀念帶入
#My platform is win32
