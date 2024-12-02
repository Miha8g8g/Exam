# Використовуємо офіційний Python образ
FROM python:3.13

# Встановлюємо робочий каталог
WORKDIR /app

# Копіюємо файли програми в контейнер
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо команду для запуску програми
CMD ["python", "Exam.py"]
