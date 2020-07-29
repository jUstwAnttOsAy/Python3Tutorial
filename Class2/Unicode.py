text='測試'
print(type(text)) #<class 'str'>
print(len(text)) #2

print('元'.encode('Big5')) #b'\xa4\xb8'
print('元'.encode('UTF-8')) #b'\xe5\x85\x83'
print('元'.encode('Big5').decode('Big5')) #元