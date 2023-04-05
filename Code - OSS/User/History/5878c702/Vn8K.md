
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