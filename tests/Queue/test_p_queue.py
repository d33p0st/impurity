from modstore.python import PriorityQueue, priority

def generator(x: int) -> int:
    return x + 5

p_queue = PriorityQueue(capacity=2, type=int, priority_generator=generator, priority_checker=priority.reverse)
p_queue_inf = PriorityQueue(type=int, priority_generator=generator, priority_checker=priority.default)

def test_p_queue():
    assert p_queue.enqueue(10)
    assert p_queue.__priority__() == [15]
    assert p_queue._priority_book == [15, None]

    assert p_queue.enqueue(20)
    assert p_queue.__priority__() == [25, 15]
    assert p_queue.__queue__() == [20, 10]

    assert p_queue_inf.enqueue(10)
    assert p_queue_inf.enqueue(20)

    assert p_queue_inf.__priority__() == [15, 25]
    assert p_queue_inf.__queue__() == [10, 20]