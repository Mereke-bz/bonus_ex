my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

top_3_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print("Три ключа с наибольшими значениями:", top_3_keys)