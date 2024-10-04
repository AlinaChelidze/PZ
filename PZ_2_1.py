N = int(input("Введите количество секунд с начала суток: "))
seconds_in_hour = 3600
seconds_since_last_hour = N % seconds_in_hour
print(f"Количество секунд, прошедших с начала последнего часа: {seconds_since_last_hour}")