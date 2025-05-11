data = []

while True:
    user_input = input("Masukkan bilangan (atau ketik 'done' bila sudah selesai): ")
    if user_input.lower() == "done":
        break
    number = int(user_input)
    data.append(number)

if data:
    rata_rata = sum(data) / len(data)
    print(f"Rata-rata: {rata_rata}")