from modstore import Queue

queue_inf = Queue(type=int) # infinite capacity
queue = Queue(capacity=1, type=int) # capacity 5

def test_queue():
    assert not queue
    assert not queue_inf

    assert queue_inf.enqueue(1)
    assert queue_inf.rear == 1
    assert queue.enqueue(1)
    assert queue_inf.enqueue(2)
    assert not queue.enqueue(2)

    assert queue != queue_inf
    assert queue
    assert queue_inf

    assert queue_inf.dequeue() == 1 # front
    assert queue_inf.enqueue(3)
    assert queue_inf.enqueue(4)

    assert queue_inf.dequeue(fro='rear') == 4 # rear

    assert queue.dequeue() == 1 # circular queue

    assert queue_inf.isNotEmpty
    assert queue.isEmpty
    
    assert queue_inf.enqueue(10, at='front') 
    assert queue_inf.front == 10