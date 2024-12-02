def arithmetic_progression_sum(p):
    a1 = 2  # Перший член
    d = 2   # Різниця прогресії

    if p <= 0:
        raise ValueError("Кількість членів прогресії повинна бути більшою за 0.")
    
    # Обчислюємо суму за правильною формулою
    sp = (p / 2) * (2 * a1 + (p - 1) * d)

    return sp

if __name__ == "__main__":
    
    p = 10  
    result = arithmetic_progression_sum(p)
    print(f"Сума перших {p} членів арифметичної прогресії: {result}")
