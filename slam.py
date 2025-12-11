slambook = []

while True:
    dctnr = {}

    dctnr["Name"] = input("Your name?...")
    dctnr["Age"] = int(input("Your age?..."))
    dctnr["date of Birth"] = input("Date of birth? dd/mm/yy...")
    dctnr["Color"] = input("Favorite color?...")
    dctnr["Message"] = input("Leave a message!...")

    slambook.append(dctnr)

    again = input("New entry : Yes/No (Capitalize first letters)...")

    if again == "No":
        break

for dctnr in slambook:
    print("\n-------SLAM BOOK!-------")
    for label, value in dctnr.items():
        print(f"{label}: {value}")