
def arithmetic_progression_sum(p):
    if p <= 0:
        raise ValueError("Кількість членів прогресії повинна бути додатним числом.")
    
    a1 = 2  # Перший член
    d = 2   # Різниця прогресії

    # Обчислюємо p-й член прогресії
    ap = a1 + (p - 1) * d

    # Обчислюємо суму
    sp = (p / 2) * (a1 + ap)

    return sp

