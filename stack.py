stack = []

# Push operation
def push():
    value = int(input("Enter value: "))
    stack.append(value)
    print("Pushed:", value)


def pop():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Popped:", stack.pop())


def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top Element:", stack[-1])


while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        print("Stack:", stack)
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
