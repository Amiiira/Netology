"""
Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. 
Функция test в коде ниже также должна отработать без ошибок.
"""


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.full_list = []
        self.index_of_list = 0
        self.index_within_list = 0
        return self

    def __next__(self):
        if self.index_of_list < len(self.list_of_list):
            current_list = self.list_of_list[self.index_of_list]
            if self.index_within_list < len(current_list):
                item = current_list[self.index_within_list]
                self.index_within_list += 1
                return item
            else:
                self.index_of_list += 1
                self.index_within_list = 0
                return next(self)
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]
    print("Test passed well!")


if __name__ == "__main__":
    test_1()
