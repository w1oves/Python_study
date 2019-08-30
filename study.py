from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':10}
point=False
wei=0
def str2float(s):
    global point
    global wei
    wei=0
    point=False
    def char2num(x):
        return DIGITS[x]
    def fn(x,y):
        global point
        global wei
        if y==10:
            point=True
            return x
        if point:
            wei+=1
        return x*10+y
    return (reduce(fn,map(char2num,s))/pow(10,wei))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')