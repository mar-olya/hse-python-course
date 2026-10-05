"""
ДЗ презентации 2, повышенный уровень, задача 1.
Время: 20–30 минут.

Тема: арифметические операторы, // и %.

Условие:
    Дано целое число секунд. Переведите его в формат ЧЧ:ММ:СС.
    Используйте только // и %.

Пример:
    In: 3661
    Out: 01:01:01
"""

def seconds_to_hms(seconds: int) -> str:
   hour = seconds // 3600 
   minu = (seconds % 3600) // 60
   sec = seconds % 60

   return f'{hour:02}:{minu:02}:{sec:02}'



if __name__ == "__main__":
    assert seconds_to_hms(3661) == "01:01:01"
    assert seconds_to_hms(0) == "00:00:00"
    assert seconds_to_hms(59) == "00:00:59"
    assert seconds_to_hms(3600) == "01:00:00"
    print("task_01 (p2 advanced): тесты пройдены")