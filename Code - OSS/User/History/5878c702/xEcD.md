
# Datetime. Работа с датой и временем

Для работы с датой и временем в Python присутствует встроенный модуль ```datetime```.

В модуле есть классы, которые позволяют получать:

- ```date``` - дату
- ```time``` - время
- ```datetime``` - дату и время

## Получение текущих данных

Получить текущие дату и время:

```Python
import datetime
current_datetime = datetime.datetime.now()

print(current_datetime)
```

Вывод:

```text
2022-10-30 16:52:51.208467
```

---

Получить текущую дату:

```Python
import datetime
current_date = datetime.date.today()

print(current_date)
```

Вывод

```text
2022-10-30
```

---
Полчить текущее время:

```Python
import datetime
current_datetime = datetime.datetime.now()
current_time = current_date_time.time()

print(current_time)
```

Вывод:

```text
16:58:12.687908
```

## Создание объектов ```datetime```

Порой необходимо создавать собстенные объекты с датой или временем. Для создания объекта с временем необходимо воспользоваться классом ```time```:

```Python
import datetime
lesson_start = datetime.time(8,45,00)

print(lesson_start)
```

Вывод:

```text
8:45:00
```

Для создания собственного объекта с датой необходимо воспользоваться классом ```date```:

```Python
import datetime
my_birthday = datetime.datetime(2000,6,28)

print(my_birthday)
```

Вывод:

```text
2000-06-28 00:00:00
```