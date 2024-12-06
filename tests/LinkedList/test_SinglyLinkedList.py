from modstore import SingleLinkNode, LinkedListOne, LinkedListError

## Test Single Link Node Functions ##

# Init
DEMO_SLN_1 = SingleLinkNode(10, SingleLinkNode(20, SingleLinkNode(30, SingleLinkNode(40))))
DEMO_SLN_2 = SingleLinkNode(11, SingleLinkNode(19, SingleLinkNode(29, SingleLinkNode(41))))
DEMO_SLN_3 = SingleLinkNode(10, SingleLinkNode(11, SingleLinkNode(20, SingleLinkNode(30))))
DEMO_SLN_4 = SingleLinkNode(10)
DEMO_SLN_5 = SingleLinkNode(10)
DEMO_LL_1 = LinkedListOne(DEMO_SLN_1)
DEMO_LL_2 = LinkedListOne([11, 19, 29, 41])
DEMO_LL_3 = LinkedListOne([10, 11, 20, 30])
DEMO_LL_4 = LinkedListOne(DEMO_SLN_4)
DEMO_LL_5 = LinkedListOne(DEMO_LL_4)

def test_properties():
    assert DEMO_SLN_1.value == 10
    assert DEMO_SLN_1.next == SingleLinkNode(20, SingleLinkNode(30, SingleLinkNode(40)))
    assert DEMO_SLN_1.all_connected_values == [10, 20, 30, 40]

def test_print():
    assert DEMO_SLN_1.__str__() == "[10 --> [20 --> [30 --> [40 --> None]]]]"

def test_conditional():
    assert DEMO_SLN_1 < DEMO_SLN_2
    assert DEMO_SLN_4 <= DEMO_SLN_5
    assert DEMO_SLN_2 > DEMO_SLN_3
    assert DEMO_SLN_4 >= DEMO_SLN_5
    assert DEMO_SLN_2 != DEMO_SLN_5
    assert DEMO_SLN_5 == DEMO_SLN_4

## Test LinkedListOne ##

def test_types_and_properties():
    assert DEMO_LL_1.head == DEMO_SLN_1
    assert type(DEMO_LL_1.head) == SingleLinkNode
    assert DEMO_LL_1.length == 4
    assert DEMO_LL_1.values == [10, 20, 30, 40]
    assert DEMO_LL_1.links == [DEMO_SLN_1, DEMO_SLN_1.next, DEMO_SLN_1.next.next, DEMO_SLN_1.next.next.next]
    DEMO_LL_1.remove_from_end
    assert DEMO_LL_1.values == [10, 20, 30]
    DEMO_LL_1.remove_from_beginning
    assert DEMO_LL_1.values == [20, 30]
    assert DEMO_LL_1.values == DEMO_LL_1.traverse
    assert DEMO_LL_1.reversed.values == [30, 20]
    assert not DEMO_LL_1.has_cycle
    assert not DEMO_LL_1.is_empty
    DEMO_LL_1.clear
    assert DEMO_LL_1.length == 0

    DEMO_LL_test = LinkedListOne(DEMO_SLN_1)

    assert DEMO_LL_test.middle == SingleLinkNode(20, SingleLinkNode(30, SingleLinkNode(40)))

def test_conditional_():
    assert DEMO_LL_1 <= DEMO_LL_2
    assert DEMO_LL_2 >= DEMO_LL_1

def test_remove():
    DEMO_LL_2.remove_at(idx=1)
    assert DEMO_LL_2.values == [11, 29, 41]
    DEMO_LL_2.remove(11)
    assert DEMO_LL_2.values == [29, 41]
    DEMO_LL_2.remove_at(idx=-2)
    assert DEMO_LL_2.values == [41]

def test_insert():
    DEMO_LL_2.insert_at(11, SingleLinkNode(20), idx=100)
    assert DEMO_LL_2.values == [41, 11, 20]

    DEMO_LL_2.insert_at(node=SingleLinkNode(100, SingleLinkNode(105)), idx=100)
    assert DEMO_LL_2.values == [41, 11, 20, 100, 105]

    DEMO_LL_2.insert_at(node=SingleLinkNode('hehe'), idx=1)
    assert DEMO_LL_2.values == [41, 'hehe', 11, 20, 100, 105]

def test_search():
    assert DEMO_LL_5.search(DEMO_LL_4) == 0
    assert DEMO_LL_5.search(DEMO_SLN_4) == 0
    assert DEMO_LL_3.search(11) == 1
    assert DEMO_LL_5.search(100) == None

def test_get_node():
    assert DEMO_LL_5.get_node(idx=0) == DEMO_LL_5.head
    try:
        DEMO_LL_1.get_node(idx=2)
    except LinkedListError:
        assert True

def test_sort():
    DEMO_LL_2.remove('hehe')
    DEMO_LL_2.sort()
    assert DEMO_LL_2.values == [11, 20, 41, 100, 105]