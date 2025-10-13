# 79p 문제 05번
# 큐를 이용한 피보나치 수 구하기

from CircularQueue import CircularQueue
Q = CircularQueue()
Q.enqueue(0)
Q.enqueue(1)
print("F(0) = 0")
print("F(1) = 1")

for i in range(2, 20) :
    val = Q.dequeue() + Q.peek()
    Q.enqueue(val)
    print("F(%d) = "%i, val)