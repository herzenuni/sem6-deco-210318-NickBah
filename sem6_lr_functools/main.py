import functools

###########################################

# Реализуем обобщенную функцию
@functools.singledispatch
def mult(obj):
        type_name = type(obj).__name__
        assert False, "Unsupported object type : " + type_name

# Для списков
@mult.register(list)
def _(obj):
    return functools.reduce(lambda acc, x: acc*x, obj)

# Для строки
@mult.register(str)
def _(obj):
    lst = obj.split(',')
    return functools.reduce(lambda acc, x: int(acc)*int(x), lst)

# Для кортежей
@mult.register(tuple)
def _(obj):
    return functools.reduce(lambda acc, x: acc*x, obj)

# Для множеств
@mult.register(set)
def _(obj):
    return functools.reduce(lambda acc, x: acc*x, obj)

# Для словарей
@mult.register(dict)
def _(obj):
    lst = list(obj.values())
    return functools.reduce(lambda acc, x: acc*x, lst)

##############################################

print(mult([1,2,3,4,5]))
print(mult('1,2,3,4,5'))
print(mult((1,2,3,4,5)))
print(mult({1, 2, 3, 4, 5}))
print(mult({0 : 1, 1 : 2, 2 : 3, 3 : 4, 4 : 5}))
print(mult({'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}))