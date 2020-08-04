#Function
def max(a, b):
    return a if a>b else b
#def 為Function定義的開頭, 後面接著函式內容, 可以參考下方VSCode提供的Code Snippet
'''
def funcname(parameter_list):
    pass
'''
#Function是對流程的抽象, 同時也是一個值
maximun = max
print(maximun(10,20)) #將max值賦予給maximun變數
#20
lambda a,b: a if a>b else b  #使用lambda, 可參考下方Code snippet
# lambda parameter_list: expression
#同樣可以賦予給變數
min = lambda a,b: a if a<b else b
minimum = min
print(min(10,20))
#10
print(minimum(10,20))
#10
