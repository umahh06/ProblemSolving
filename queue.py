queue = []


def enqueue():
    value = int(input("Enter value: "))
    queue.append(value)
    print("Inserted:", value)


def dequeue():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Deleted:", queue.pop(0))


def peek():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Front Element:", queue[0])


while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        print("Queue:", queue)
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
