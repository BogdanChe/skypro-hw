def bank(X, Y):
    total = X
    for _ in range(Y):
        total += total * 0.10  # добавляем 10% к общей сумме каждый год
    return total

# Пример использования функции
X = 1000  # размер вклада
Y = 5     # срок вклада в годах
result = bank(X, Y)
print("Сумма на счету спустя", Y, "лет будет равна", result, "рублей.")
