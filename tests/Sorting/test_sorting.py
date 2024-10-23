from modstore.algorithms.sorting import Sort, SortObject

def test_all():
    for attribute in Sort.__dict__.keys():

        if attribute.endswith('_sort'):

            DATA_INT = [5, 4, 2, 3, 1]
            DATA_INT_SORTED = [1, 2, 3, 4, 5]
            DATA_STR = ['e', 'd', 'b', 'c', 'a']
            DATA_STR_SORTED = ['a', 'b', 'c', 'd', 'e']

            check = False
            for x in ['tag']:
                if attribute.__contains__(x):
                    check = True
                    break
            
            if check:
                continue

            print(f"testing: {attribute}")
            
            assert getattr(Sort, attribute)(DATA_INT, reverse=True) == [5, 4, 3, 2, 1]
            assert getattr(Sort, attribute)(DATA_INT) == DATA_INT_SORTED
            if 'count' not in attribute and 'radix' not in attribute and 'bucket' not in attribute and 'pigeon' not in attribute and 'sleep' not in attribute:
                assert getattr(Sort, attribute)(DATA_STR, reverse=True) == ['e', 'd', 'c', 'b', 'a']
                assert getattr(Sort, attribute)(DATA_STR) == DATA_STR_SORTED