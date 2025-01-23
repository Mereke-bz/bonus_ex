example_dict = {'a': 3, 'b': 1, 'c': 2}


ascending = dict(sorted(example_dict.items(), key=lambda item: item[1]))
print("Словарь по возрастанию значений:", ascending)

descending = dict(sorted(example_dict.items(), key=lambda item: item[1], reverse=True))
print("Словарь по убыванию значений:", descending)