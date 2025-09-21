# Uppgift 5 – Simple Contact List Manager

## Beskrivning
Ett menybaserat program som låter användaren bygga och hantera en kontaktlista med en vanlig Python-lista.

### Funktioner
1. **Add a contact** – lägger till ett namn (förhindrar dubletter)
2. **Show all contacts** – skriver ut alla kontakter (sorterat alfabetiskt)
3. **Search for a contact** – case-insensitiv sökning i listan
4. **Remove a contact** – tar bort ett namn om det finns
5. **Quit** – avslutar programmet

---

## Så här kör du
Öppna terminalen i mappen där filen ligger:
```bash
py Uppgift5.py
```
(eller `python Uppgift5.py`)

---

## Exempel
```
==== CONTACT LIST ====
1. Add a contact
2. Show all contacts
3. Search for a contact
4. Remove a contact
5. Quit
Choose an option: 1
Enter name: Alice
Added: Alice

Choose an option: 2
Contacts:
- Alice
```

---

## Bonus
- Förhindrar dubletter (case-insensitivt)
- Bekräftelse vid add/remove
- Utskrift sorterad alfabetiskt

---

## Filstruktur
```
Uppgift-5/
│
├── Uppgift5.py    # Själva programmet
└── README.md      # Denna fil
```

---

## Författare
- Lucas Bergman
