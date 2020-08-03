# 目前Python支援的容器型態有list, set, dict, tuple

#list 有序且可變群集
print(len([0,1,2,3])) #len回傳長度
#4
print([0,1]+[2,3]) #「+」可以串聯字串
#[0,1,2,3]
print([0]*5) #「*」可以複製陣列
#[0,0,0,0,0]
numItem =[0,1,2,3,4,5,6,7]
print(numItem[-1]) #負數表倒數
#7
nameItem = ['Steve', 'Bob', 'Alex', 'Kevin']
print(', '.join(nameItem)) #以逗號串聯,注意!list中必須要為字串才可以使用
#Steve, Bob, Alex, Kevin
print(list('Steve')) #列出字串中的每個字元
#['S', 't', 'e', 'v', 'e']

#Set 無序、hashable
admins = {'Justin', 'caterpillar'} #建立set
users = {'momor', 'hamini', 'Justin'}
print('Justin' in admins) #Justin是否在admin中
#True
print(admins & users) #同時在admins及users
#{'Justin'}
print(admins|users) #是admin或users
#{'hamini', 'Justin', 'momor', 'caterpillar'}
print(admins-users) #是admins不是users
#{'caterpillar'}
print(admins ^ users) #XOR運算, 只在單一一個Set中
{'caterpillar', 'momor', 'hamini'}
print(admins>users) #∈ =>不清楚什麼意思, 代補
#False
print(admins<users) #∈ =>不清楚什麼意思, 代補
#False

#dict 必須hashable, 類似C#的Dictionary
passwords = {'Justin':123456, 'caterpillar':987654321}
print(passwords['Justin']) 
#123456
passwords["Steve"] = '0520' #可以自己增加內容
print(passwords)
#{'Justin': 123456, 'caterpillar': 987654321, 'Steve': '0520'}
del passwords['caterpillar'] #刪除
print(passwords)
# {'Justin': 123456, 'Steve': '0520'}
print(passwords.items())
#dict_items([('Justin', 123456), ('Steve', '0520')])
print(passwords.keys()) #只列出key
#dict_keys(['Justin', 'Steve'])
print(passwords.values()) #只列出value
#dict_values([123456, '0520'])
#上述3種方法可使用list()轉換成lsit
print(list(passwords.items()))
#[('Justin', 123456), ('Steve', '0520')]
print(passwords.get('Marry', "doesn't exists")) #避免不存在的key出現, 使用get找不到時會回傳預設值
#doesn't exists

#tuple 不可變的, 其它操作跟list一樣, 相較於list有較好的效能
nameList = ('Steve', 'Bob', 'Marry')
print(nameList)

#if, for, while
#同一區塊必須使用相同的區塊標示(Tab或4空格)

#if
from sys import argv
if len(argv)>1:
    print('Hello, ', argv[1])
else:
    print('Hello, Guest')
#Hello, Guest

#if 縮寫
from sys import argv
print('Hello, ', argv[1] if len(argv)>1 else 'Guest') #使用 [結果A] if [條件] else [結果B]
#Hello,  Guest

#for
numbers = [10, 20, 30]
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)
#[100, 400, 900]

#for 縮寫
numbers = [10, 20, 30]
print([number ** 2 for number in numbers]) #使用[執行內容] for [變數] in [集合]
#[100, 400, 900]

#for+if
numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
odd_numbers = []
for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)
print(odd_numbers)
#[11, 45, 1, 3, 7, 9]

#for+if縮寫
numbers = [11, 2, 45, 1, 6, 3, 7, 8, 9]
print([number for number in numbers if number%2!=0]) #如果只是單純輸入條件成立 [結果A] for [變數] in [集合] if [條件]
#[11, 45, 1, 3, 7, 9]
print([number if number%2!=0 else 'XX' for number in numbers]) #條件成立與不成立皆要輸出結果 [結果A] if [條件] else [結果B] for [變數] in [集合]
#[11, 'XX', 45, 1, 'XX', 3, 7, 'XX', 9]

#巢狀結構平坦化
lts = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([ele for lt in lts for ele in lt]) # [子變數] for [變數] in [集合] for [子變數] in [變數]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

#使用[]直接產生list, 如上方案例
#使用{}產生set, 會自動把重複項移除
lts = [[1, 2, 3,4], [1,4, 5, 6], [2,5,6,7, 8, 9]]
print({ele for lt in lts for ele in lt})
#{1, 2, 3, 4, 5, 6, 7, 8, 9}

#甚至可以建立dict實例
names = ['caterpillar', 'justin', 'openhome']
passwds = [123456, 654321, 13579]
print({name : passwd for name, passwd in zip(names, passwds)}) 
#{'caterpillar': 123456, 'justin': 654321, 'openhome': 13579}
#由後往前看先zip集合, 建立tuple, 再使用 [dict] for [集合1], [集合2] in [tuple], 完成dict實例

#Example, 將以下輸入已一行程式搞定
numbers = []
for number in range(20):
    numbers.append(str(number))
print(", ".join(numbers))
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
# 結果如下
print(', '.join([str(number) for number in range(20)]))
#0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
