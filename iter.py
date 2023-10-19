class FlatIterator:

    def __init__(self, list_of_list):
        self.lst = list_of_list

    def __iter__(self):
        self.len_lst = [len(i) - 1 for i in self.lst]
        self.len_lol = len(self.lst)
        self.x = 0
        self.y = -1
        return self

    def __next__(self):
        if self.y == self.len_lst[self.x]:
            self.y = 0
            self.x += 1
            if self.x == self.len_lol:
                raise StopIteration
        else:
            self.y += 1
        item = self.lst[self.x][self.y]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()