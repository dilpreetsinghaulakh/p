SIZE = 5
buffer = []
count = 0

def produce():
    global count
    if count < SIZE:
        print(f"Produced: {count + 1}")
        buffer.append(count + 1)
        count += 1
    else:
        print("Buffer full, cannot produce.")

def consume():
    global count
    if count > 0:
        item = buffer.pop(0)
        print(f"Consumed: {item}")
        count -= 1
    else:
        print("Buffer empty, cannot consume.")

def main():
    while True:
        print("\n1. Produce\n2. Consume\n3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            produce()
        elif choice == 2:
            consume()
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()