# map() 会根据提供的函数对指定序列做映射。
#map(function, iterable, ...) function -- 函数 iterable -- 一个或多个序列
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

arr = [1,2,3,4,5]
squre_arr = list(map(lambda x: x**2,arr))
print(squre_arr)

# sorted(iterable, cmp=None, key=None, reverse=False)
d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序