def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    try:
        n = int(input("Введите количество чисел: "))
        if n <= 0:
            print("Количество чисел должно быть положительным.")
            return

        numbers = []
        for i in range(n):
            num = float(input(f"Введите число {i+1}: "))
            numbers.append(num)

        sorted_numbers = bubble_sort(numbers)
        print("Отсортированные числа:", sorted_numbers)

    except ValueError:
        print("Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    main()
