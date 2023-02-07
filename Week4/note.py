Q = [1,2,3,4,5,6]
while len(Q) > 1:
    Q.enqueue(Q.dequeue())
    Q.dequeue()
    print(Q)
