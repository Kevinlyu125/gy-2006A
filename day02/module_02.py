# 调用其他表的变量
# from day02 import module_01
# from day02.module_01 import a as module_01_a,b as module_b
#
# print(module_01.a)
# module_01.b()
# print(module_01.test.name)
# if __name__ == '__main__':
#     print(module_01.a)
#     module_01.b()


# 格式转换
a = 123
b = "564"

# print(a + int(b))
# print(str(a) + b)
#
# x = [21,31321,321,1,32]
# y = (1,21,132,13)
# z = {351,1,21,}
# # 字符串转列表
# print(list(b))
# # 元组转列表
# print(list(y))
# #列表转元组
# print(tuple(x))
# #元组转集合
# print(set(y))
# #集合转列表
# print(list(z))

# # 打开模式：r 读取  w 清空写入 a 追加写入 b 二进制模式
#
# f = open ("1.txt",'w') # open 打开文件
# f.write("规划""\n""safd") # write 写入内容至打开的文件
# f.close() # 关闭文件
#
#
# # 写入多行  01
# b = '''dfadfa
# dsfsf
# sdfsf
# sdfs
# '''
# f = open ("1.txt",'w')
# f.write(b)
# f.close()

# # 写入多行  02
# f = open ("1.txt",'w')
# # f.write("sadfaf\ndsfsffdsf\nsdfsfs\nsadaserrre")
# f.writelines(["SADAD\n","fdsdfsdf\n","asdfasf\n"])
# f.close()




# # 字符串的截取操作
# a ="hjdsgfhdshdsfsdgdfjks"
# print(a[0])    # 截取光标为0位的字符
# print(a[-1])     # 截取光标为-1（最后一位）位的字符
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-3])


# # 通过占位符格式化
# for i in range (1,10):
#     for j in range (1,i+1):
#         print ("%d * %d = %d"%(i,j,i*j) ,end="\t")
#     print ()


# 通过.format 格式化
# for i in range (1,10):
#     for j in range (1,i+1):
#         print ("{} * {} = {}".format(i,j,i*j) ,end="\t")
#     print ()

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

# a =[2313,1231,3,13,1,1231,32]
# a[0] = 1
# print(a)
#
# a[0:6] = 1,5,21,1,23
# print(a)
#
# a [-1] = 56
# print(a)
#
# a[-1:-3:-1] =55,66
# print(a)

# print("{:^10}".format(1213))
# print("{:.2f}".format(3.1415926))

# # 列表增加数据
# l = [21,31,231,1,3]
# # print(l)
# # l.append(212)
# # l.extend(('21313',213))
# l.insert(0,"123")
# l.insert(5,"王大锤")
# print(l)

# # 列表删数据  pop
# l = [21,31,231,1,3]
# print(l.pop())
# print(l)
# print(l.pop(1))
# print(l)

             # remove
# l =[2,131,3,1,12,1,132,121]
# l.remove(2)
# print(l)
# l.remove(1)     # 如果列表里面有多个相同的值 删除只会删除第一个数据
# print(l)

# l =[True,2,131,3,1,12,1,132,121]   #python ture = 1 flase = 0
# l.remove(1)
# print(l)
#
# l.clear()             # 删除整张表
# print(l)


# # 元组常见操作       遍历   修改值   增加
# d = {"name":"小明","age":18,"sex":"男"}
# for key in d:
# 	print(d[key])
#
#
# d["age"]="22"
# print(d)
#
# d["addr"] = "上海闵行"
# print(d)
#
# d.update({"addr":"上海浦东","学历":"本科"})
# print(d)

# d = {"name":"小明","age":18,"sex":"男"}
# s = {}
# for key in d:
#     if key.startswith("a"):
#         continue
#
#         s[key] = d[key]
# print(s)



# def shang_yu(a,b):
#     try:
#         return ("商： ", a // b, "余数: ", a % b)
#     except:
#         return
#
# print(shang_yu(10,20))


# print(1/0)

# def shang(a,b):
#     try:
#         return ( a / b)
#     except  ZeroDivisionError:
#         return
#
# print(shang(1,0))


# def shang(a,b):
#     try:
#         print ( a / b)
#     except  ZeroDivisionError as e :
#         print(e)
#     else:
#         print("除法执行成功")
#     finally:
#         print("无论语法有没有问题都会执行")
#
# print(shang(10,2))

class c (Exception):
    def __init__(self,value= "值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 1
try:
    if a == 0:
        print("a = {} 触发异常".format(a))
        raise  c
    print("a = {} 未触发异常".format(a))
except c as e:
    print(e)
