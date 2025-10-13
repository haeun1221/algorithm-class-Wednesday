# 파이썬을 이용하여 선형 큐 구현하기

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is Full")
        
        self.queue[self.rear] = item
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        return self.queue[self.front]

    def __len__(self):
        return self.rear - self.front

#--------------------------------------------------------------------------------
# 67p 퀴즈2번

try:
    # 최대 크기 8인 큐 생성
    my_queue = ArrayQueue(8)
    my_queue.front = 6
    my_queue.rear = 6

    # 요소 삽입 (Enqueue)
    my_queue.enqueue(10)
    my_queue.enqueue(11)
    my_queue.enqueue(12)
    my_queue.enqueue(13)
    my_queue.dequeue()
    my_queue.dequeue()

    print(f"연산 처리 후 front: {my_queue.front}")
    print(f"연산 처리 후 rear: {my_queue.rear}")

except Exception as e:
    print(f"오류 발생: {e}")