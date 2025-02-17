
queueArr = [1,2,3,4,5]

front = 0
rear = 4
size = 5

def isFull():
    global size
    if size == 5:
        return True
    
def isEmpty():
    global size
    if size == 0:
        return True

def Dequeue():
    global front
    global rear
    global size
    if isEmpty() != True:
        temp = queueArr[front]
        queueArr[front] = None
        front = front + 1
        size = size - 1
        print(temp, "has been dequeued")
    else:
        print("There are no elements in the queue")

def Enqueue(myElement):
    global front
    global rear
    global size
    if isFull() != True:
        rear = rear + 1
        if rear > size -1:
            rear = 0
            size = size + 1
            queueArr[rear] = myElement
            print(myElement,"has been enqueued")
                
    else: 
        print("The queue is full, element cannot be enqueued")

Dequeue()
Enqueue(13)
Enqueue(15)
print(queueArr)

