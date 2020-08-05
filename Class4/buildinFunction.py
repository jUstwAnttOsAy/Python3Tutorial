# 內建的幾個好用函式
#range、zip、enumerate
names = ['Justin', 'caterpillar', 'openhome']
#結果
'''
0, Justin
1, caterpillar
2, openhome 
'''
#range
for item in range(3):
    print('{0}, {1}'.format(item, names[item]))
#zip
for item in list(zip(range(3), names)):
    print('{0}, {1}'.format(item[0], item[1]))
#enumerate
for item in list(enumerate(names)):
    print('{0}, {1}'.format(item[0], item[1]))

#過濾長度6的元素
#一般寫法
lt = ['Justin', 'caterpillar', 'openhome']
morethanSix = []
for item in lt:
    if len(item)>6:
        morethanSix.append(item)
print(morethanSix)
#先封裝函式, 再執行
def filter_lt(predicate, lt):
    result = []
    for ele in lt:
        if predicate(ele):
            result.append(ele)
    return result
print(filter_lt(lambda item: len(item)>6, lt)) #長度大於6
print(filter_lt(lambda item: 'i' in item, lt)) #包含i

#轉成大寫
def map_lt(mapper, lt):
    result = []
    for ele in lt:
        result.append(mapper(ele))
    return result

print(map_lt(lambda item: item.upper(), lt)) #轉成大寫

#Python本身有提供fliter、map功能
print(list(filter(lambda ele: len(ele)>6, lt))) #大於6
print(list(filter(lambda ele: 'i' in ele, lt))) #包含i
print(list(map(lambda ele: ele.upper(), lt))) #轉成大寫
print(list(map(lambda ele: len(ele), lt))) #轉成長度

#fliter及map回傳的並不是list是Generator, 所以需要使用list()轉換, 只有真正需要時才會進行轉換, 稱為惰性求值(Lazy evaluation)
#使用for產生list
print([ele for ele in lt if len(ele) > 6])
print([ele for ele in lt if 'i' in ele])
print([ele.upper() for ele in lt])
print([len(ele) for ele in lt])
#使用for產生Generator, 將[]改成()
print((ele for ele in lt if len(ele) > 6))
print((ele for ele in lt if 'i' in ele))
print((ele.upper() for ele in lt))
print((len(ele) for ele in lt))

#建議將lambda進行命名, 增加可讀性
getLen = lambda ele: len(ele)
print(list(map(getLen, lt)))

#reduce
import functools
print(functools.reduce(lambda sum, elem:sum+elem, [1,2,3,4,5], 0)) #將list值相加
#15
#將lambda命名後
sumList = lambda sum, elem: sum+elem
print(functools.reduce(sumList, [0,1,2,3,4,5],0)) #reduce([處理函式], [list], [初始值]), 處理過程為[處理函式]([初始值],[list][0]) = [結果A] => [處理函式]([結果A],[list][1])....

#練習reduce, 將下方程式迴圈部分已reduce重構
def ascending(a, b): return a - b
def descending(a, b): return -ascending(a, b)
'''
# selection sort
def sorted(xs, compare = ascending):
    return [] if not xs else __select(xs, compare)

def __select(xs, compare):
    selected = xs[0]
    for elem in xs[1:]:
        if compare(elem, selected) < 0:
            selected = elem

    remain = []
    selected_list = []
    for elem in xs:
        if elem != selected:
            remain.append(elem)
        else:
            selected_list.append(elem)

    return xs if not remain else selected_list + __select(remain, compare)

print(sorted([2, 1, 3, 6, 5]))
print(sorted([2, 1, 3, 6, 5], descending))
#[1, 2, 3, 5, 6]
#[6, 5, 3, 2, 1]
'''
#NEW
def sorted(xs, compare = ascending):
    return [] if not xs else __select(xs, compare)

def __select(xs, compare):
    selected = functools.reduce(lambda sel, elem: elem if compare(elem, sel)<0 else sel, xs) #reduce不一定需要初始值
    '''
    selected = xs[0]
    for elem in xs[1:]:
        if compare(elem, selected) < 0:
            selected = elem
    '''
    remain = [elem for elem in xs if elem!=selected]
    selected_list = [elem for elem in xs if elem==selected]
    '''
    remain = []
    selected_list = []
    for elem in xs:
        if elem != selected:
            remain.append(elem)
        else:
            selected_list.append(elem)
    '''
    return xs if not remain else selected_list + __select(remain, compare)

print(sorted([2, 1, 3, 6, 5]))
print(sorted([2, 1, 3, 6, 5], descending))

