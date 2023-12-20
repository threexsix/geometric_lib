# Geometric Lib

Этот проект создан для вычисления площади и периметра различных геометрических фигур. 

## Функции

### `area(...params)`
Данная функция вычисляет площади фигуры.
- `...params` : параметры, зависящие от типа фигуры.


Пример использования с квадратом:

```python
# Импорт модуля square
from geometric_lib import square

# Вызов функции для вычисления площади
result = square.area(5)

# Вывод результата
print(result)
```

### `perimeter(...params)`
- `...params` : параметры, зависящие от типа фигуры.


Данная функция вычисляет периметр фигуры.

Пример использования с треугольником:

```python
# Импорт модуля square
from geometric_lib import triangle

# Вызов функции для вычисления площади
result = triangle.perimeter(1, 2, 3)

# Вывод результата
print(result)
```
## Тесты
Ran 24/24 tests in 0.000s
- OK


## История изменений
| Хеш комита   | Тип    | Коммит                            |
|--------------|--------|-----------------------------------|
| 78cc54a      | feat   | add triangle_test.py              |
| 4050db9      | feat   | triangle value validation         |
| 7a5ee53      | feat   | add square_test.py                 |
| 07a7abb      | feat   | square value validation            |
| 591c23b      | feat   | add rectangle_test.py              |
| ebefe6d      | feat   | rectangle value validation         |
| b6724fb      | feat   | add circle_test.py                 |
| a8a2941      | feat   | circle value validation            |

