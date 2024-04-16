total_sum = 0
current_number = 50
iteration = 1

while total_sum <= 1000:
    total_sum += current_number 
    print(f"{iteration}.", end=" ")

    for num in range(50, current_number + 1):
        print(num, end=" ")
        if num < current_number:
            print("+", end=" ")

    print(f"= {total_sum}")
    current_number += 1
    iteration += 1
