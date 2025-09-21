# Uppgift5.py
# Programmering 1 – Moment 5: Practical Exercises
# Övningar med listor

def exercise_1():
    colors = ["red", "blue", "green"]
    print("Colors list:", colors)

def exercise_2():
    colors = ["red", "blue", "green"]
    print("First color:", colors[0])
    print("Last color:", colors[-1])

def exercise_3():
    colors = ["red", "blue", "green"]
    print("Original list:", colors)
    colors[1] = "yellow"
    print("Updated list:", colors)

def exercise_4():
    colors = ["red", "blue", "green"]
    colors.append("purple")
    colors.remove("red")
    print("Updated list:", colors)

def exercise_5():
    colors = ["red", "blue", "green"]
    for c in colors:
        print("Color:", c)

def exercise_6():
    names = []
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        names.append(name)
    print("All names:", names)
    return names

def exercise_7():
    names = []
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        names.append(name)
    print("All names:", names)
    print("Total names:", len(names))
    return names

def exercise_8():
    names = []
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        names.append(name)
    search = input("Enter a name to search for: ")
    if search in names:
        print(search, "is in the list!")
    else:
        print(search, "is NOT in the list.")

def bonus():
    numbers = [5, 3, 8, 3, 2, 5, 1, 8, 2]
    unique_sorted = sorted(set(numbers))
    print("Original list:", numbers)
    print("Without duplicates, sorted:", unique_sorted)


# --- Meny ---
def menu():
    while True:
        print("\n==== MENU (Uppgift 5) ====")
        print("1. Exercise 1: Create a list")
        print("2. Exercise 2: Access list items")
        print("3. Exercise 3: Update list item")
        print("4. Exercise 4: Add and remove items")
        print("5. Exercise 5: Loop through list")
        print("6. Exercise 6: Build a list from user input")
        print("7. Exercise 7: Count items")
        print("8. Exercise 8: Check if value exists")
        print("9. Bonus: Sort and remove duplicates")
        print("0. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            exercise_1()
        elif choice == "2":
            exercise_2()
        elif choice == "3":
            exercise_3()
        elif choice == "4":
            exercise_4()
        elif choice == "5":
            exercise_5()
        elif choice == "6":
            exercise_6()
        elif choice == "7":
            exercise_7()
        elif choice == "8":
            exercise_8()
        elif choice == "9":
            bonus()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
