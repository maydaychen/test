a = input("请输入一个整数")
b = input("请输入另一个整数")
try:
    c = int(a) + int(b)
except ValueError:
    print("请输入数字！")
else:
    print(c)
