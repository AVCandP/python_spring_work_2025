# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
#
# Преобразуйте переменную flag в Boolean
# flag = 1
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
#
# Преобразуйте значение 0 и 1 в Boolean
#
# Преобразуйте False в строку

age = "23"
age_int = int(age)
print(age_int)
print(type(age_int))

foo = "23abc"
foo_int = int(foo, 16)
print(foo_int)
print(type(foo_int))

flag = 1
print(bool(flag))
print(type(bool(flag)))

str_one = "Privet"
print(bool(str_one))
print(type(bool(str(str_one))))

str_two = ""
print(bool(str_two))
print(type(bool(str(str_two))))

n1 = 1
n2 = 0
n1_bool = bool(n1)
print(n1_bool)
print(type(n1_bool))
n2_bool = bool(n2)
print(n2_bool)
print(type(n2_bool))

boo = True
str_bo = str(boo)
print(str_bo)
print(type(str_bo))
str_bo2 = str(int(boo))
print(str_bo2)
print(type(str_bo2))