def filter_strings(filter_func, string_array):
    return list(filter(filter_func, string_array))

filter_conditions = lambda s: not (' ' in s or s.startswith('a') or len(s) < 5)

filtered_strings = filter_strings(filter_conditions, ["apple", "banana", "hello", "world", "a test", "python", "code", "abc"])
print(filtered_strings)
