def second_index(text, some_str) -> None:
    if text.count(some_str) > 1:
        index_first = text.index(some_str)
        index_second = text.index(some_str, index_first+1)
        return index_second


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
