# Uppgift5.py
# Programming 1 – Moment 5: Simple Contact List Manager

def normalized(name: str) -> str:
    """Trimma mellanslag och jämna ut versaler för jämförelser."""
    return name.strip().lower()

def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("No name entered.")
        return
    # Bonus: förhindra dubletter (case-insensitivt)
    if any(normalized(name) == normalized(c) for c in contacts):
        print(f"'{name}' is already in the list.")
        return
    contacts.append(name)
    print(f"Added: {name}")

def show_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    # Bonus: sortera alfabetiskt vid utskrift (utan att ändra original-ordning)
    print("Contacts:")
    for c in sorted(contacts, key=lambda s: s.lower()):
        print(f"- {c}")

def search_contact(contacts):
    query = input("Enter name to search: ").strip()
    if not query:
        print("No name entered.")
        return
    found = any(normalized(query) == normalized(c) for c in contacts)
    if found:
        print(f"'{query}' is in the list.")
    else:
        print(f"'{query}' is NOT in the list.")

def remove_contact(contacts):
    target = input("Enter name to remove: ").strip()
    if not target:
        print("No name entered.")
        return
    # Hitta exakt match case-insensitivt och ta bort just det lagrade värdet
    for i, c in enumerate(contacts):
        if normalized(c) == normalized(target):
            removed = contacts.pop(i)
            print(f"Removed: {removed}")  # Bonus: bekräftelse
            return
    print(f"'{target}' was not found.")

def menu():
    contacts = []  # tom lista i början

    while True:
        print("\n==== CONTACT LIST ====")
        print("1. Add a contact")
        print("2. Show all contacts")
        print("3. Search for a contact")
        print("4. Remove a contact")
        print("5. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            remove_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    menu()
