def add_notes():
    note = input("Enter your note: ")
    with open("notes.txt" , "a") as file:
        file.write(note)
    print("Note Added")

def view_notes():
    try:
        with open("notes.txt" , "r") as file:
          notes = file.read()
        print(notes)

    except FileNotFoundError:
        print("No file Founded")

def main():
    while True:
        print("1. ADD NOTE")
        print("2. VIEW NOTE")
        print("3. EXIT")


        choice = int(input("Enter Your choice: "))

        if choice == 1:
            add_notes()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            print("bye bye")
            break
        else:
            print("Invalid choice")

main()

