import unittest
from Exam import arithmetic_progression_sum

class TestArithmeticProgressionSum(unittest.TestCase):
    def test_valid_input(self):
        # Перевіряємо результати для правильного вводу
        self.assertAlmostEqual(arithmetic_progression_sum(1), 2.0, places=7)  # Сума 1-го члена
        self.assertAlmostEqual(arithmetic_progression_sum(2), 6.0, places=7)  # Сума 2-х членів
        self.assertAlmostEqual(arithmetic_progression_sum(3), 12.0, places=7)  # Сума 3-х членів
        self.assertAlmostEqual(arithmetic_progression_sum(10), 110.0, places=7)  # Сума 10 членів
        self.assertAlmostEqual(arithmetic_progression_sum(1000), 1001000.0, places=7)  # Сума 1000 членів

    def test_invalid_input(self):
        # Перевіряємо виключення для неправильного вводу
        with self.assertRaises(ValueError):
            arithmetic_progression_sum(0)  # 0 членів — некоректно
        with self.assertRaises(ValueError):
            arithmetic_progression_sum(-5)  # Від’ємна кількість членів

    def test_edge_cases(self):
        # Тестуємо граничні значення
        self.assertAlmostEqual(arithmetic_progression_sum(1), 2.0, places=7)  # Мінімальний ввід

if __name__ == '__main__':
    unittest.main()
