#模組
#只要建立一個檔案, 即是建立一個Module
import xmath
#會在相同目錄下尋找xmath檔案, 找不到會在sys.path中尋找

#模組提供名稱空間
print(xmath.pi) #呼叫xmath的pi變數
#3.141592653589793
import xmath as math #可以取別名
print(math.pi)
#3.141592653589793

from xmath import min #自模組xmath匯入min方法
print(min(10,2))
#2