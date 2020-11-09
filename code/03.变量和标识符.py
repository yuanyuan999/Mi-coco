# python中使用变量不需要声明，直接为变量赋值即可
a = 10
# 不能使用没有进行过赋值的变量
# 如果使用没有赋值过的变量，会报错：NameError: name 'b' is not defined
# print(a)
# python是一个动态类型的语言，可以为变量赋任意类型的值，也可以任意修改变量的值
b = 'hello'
# print(a)
# 标识符
# 在python中所有可以自主命名的内容都属于标识符
# 比如：变量名、函数名、类名
# 标识符必须遵守标识符规范
# 1.标识符中可以包含字母、数字、下划线、但是不能以数字开头
#       例子： a_1 _a1 _1a
# 如果使用不符合标注的标识符，将会报错：SyntaxError: invalid syntax
# 2.标识符不能是python中的关键字和保留字
#      也不建议使用python中的函数名作为标识符，因为这样会导致函数被覆盖
# 3.命令规范：
#         在python中注意遵循两种命名规范：
#             下划线命名法
#                 所有字母小写，单词之间用_分割
#                   max_length
#             帕斯卡命名法（大驼峰命名法）
#                     首字母大写，每个单词开头字母大写，其余字母小写
#                     MaxLength  MinLength
print(a)
age = 18
MaxBook = 123
Age_gril = 90
