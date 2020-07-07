# a,b =10,60
# print (a,b)
# print (a % b)
# print  (a // b)


# b = ["果芽","腾讯","阿里","百度"]
#
# if ("知乎" in b):
#     print ("非合作方")
# else:
#     print ("合作方")


# result = 99
# if (result >0 and result < 60):
#         print ("不及格")
# if (result >= 60 and result < 70):
#         print ("及格")
# if (result >= 71 and result < 80):
#         print ("良好")
# if (result >= 81 and result < 100):
#         print ("优秀")



# result_l =[12,21,32,56,85,45,98,56]

# for result in result_l:
#         if (result >0 and result < 60):
#                 print ("不及格")
#         elif (result >= 60 and result < 70):
#                 print ("及格")
#         elif (result >= 71 and result < 80):
#                 print ("良好")
#         elif (result >= 81 and result < 100):
#                 print ("优秀")
#         else:
#                 print ("请输入正确的成绩")

# #range 函数
# s = 0
# for i in range (100,0,-1):
#    s = s + i
# print (s)











#
# # 求出10*9*8...*1 的值
# s = 1
# for i in range (10,0,-1):
#     s = s * i
# print (s)
#


# # 猜数字
# flag = True
# a = 29
# while flag:
#     b = int(input("请输入数字"))
#     if b > a :
#         print ("大了")
#     elif (b < a):
#         print ("小了")
#     else:
#         print ("猜对了")
#         flag =  False



# 找出100以内能被3整除的数字
#
# for i in range(1,100):
#     if (i % 3 == 0):
#         print (i)

# # continue 用法
# for i in range(1,100):
#     if (i % 3 != 0):
#         continue
#     print (i)

# #break 用法
# a = ["知乎","腾讯","阿里","果芽"]
# for i in a:
#     if(i == "果芽"):
#         print(i)
#         break


# 定义一个求两个数商数余数的办法
# def shang_yu(a,b):
#     print ("商： ",a // b,"余数: ", a % b)
#
# shang_yu(10,2)
#
#
# def shang_yu(a,b):
#     if (b == 0):
#         print ("除数不能为0")
#     else:
#         print ("商： ",a // b,"余数: ", a % b)
#
# shang_yu(10,0)


# def shang_yu(a,b):
#     if (b == 0):
#         return  None
#     else:
#        return (a // b, a %b )
#
# # res = shang_yu(2,20)   # 按照位置传参
# res = shang_yu(b = 20,a = 2)  # 按照关键字传参
#
# if res is None:
#     print ("参数错误")
# else:
#     print ("商： ",res[0], "余数: ", res[1])


# def sm (a,b=2):
#     return a + b
# print (sm(2,b=9))


# #
# def suml(name,* args,**kwargs):
#     print (name)
#     print (kwargs)
#     s = 0
#     for i in args:
#          s+=i
#     return s
# print (suml(1,2,3))
# print (suml(name = "lbw"))



# 面向对象
# 类的定义
# class cala():
#     res = None   # 类变量类的所有实例共享
#     def __init__(self,a,b):    # 魔法函数 类的实例化的时候用 又称构造函数
#         self.a =a     # 实例变量
#         self.b =b
#         # c = 10  # 局部变量
#     # def input(self,a,b):
#     #     self.a =a
#     #     self.b =b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def che(self):
#         self.res = self.a * self.b
#     def sha(self):
#         self.res = self.a // self.b
#     def yu(self):
#         self.res = self.a % self.b
#     def get_result(self):
#         print (self.res)
#
# # 类的实例化 c 就是对象
# # c = cala()
# # c.input(10,20)
# # c.sum()
# # c.get_result()
# # c.div()
# # c.get_result()
# # c.che()
# # c.get_result()
# # c.sha()
# # c.get_result()
# # c.yu()
# # c.get_result()
# #
# c = cala(10,20)
# c.sum()
# c.get_result()
#



# # 9 9 乘法表
# for i in range (1,10):
#     for j in range (1,i+1):
#         print (j,"X",i,"=",i*j,end="\t")
#     print ()


# # 冒泡排序
# l = [121,5321,31,231]
# length = len(l)
# print(length)
# # print(length)
# for i in range(length -1,0,-1):      # 外层循环确定排好序的数据下标
#     # print("i:",i)
#     # print("length-1:",length-1)
#     for j in range(i):             # 遍历未排好序的列表
#         print("j:",j)
#         if (l[j] > l[j+1]):          # 判断相邻两个数据，前边的如果大于后边的，则交换两个数据的位置
#             l[j],l[j+1] =  l[j+1],l[j]
#
# print(l)


# a = [2213,123,12,1,31]
# # length = len(a)
# # # print(length)
# # for i in range (length-1,0,-1):
# #     for j in range (i):
# #         if (a[j] > a[j+1]):
# #            a[j],a[j+1] = a[j+1],a[j]
# # print(a)


# for i in range(1,10):
#     for j in range(i):
#         print(" %d * %d = %d" % (j, i, j * i), end='\t')
#     print()


# 私有类 私有方法







#继承
# class Parent():
#     money =100000000000
#     house =352
#     __yi_wu = "衣物"
#
#     def shou_yi(self):
#         print("点石成金")
#     def __init__(self,a):
#         self.a = a
#
# class Child (Parent):
#     ai_hao ="花钱"
#     def __init__(self,a):
#         super().__init__(a)
#     pass
#
# c = Child(125)
# print(c.ai_hao)
# print(c.money)
# print(c.house)
# c.shou_yi()
# print(c.a)