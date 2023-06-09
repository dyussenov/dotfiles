tasks = [
    {
        "title": "Основы синтаксиса",
        "theory_text": "В первую очередь стоит заметить, что любая строка сама по себе является регулярным выражением. Так, выражению Хаха, очевидно, будет соответствовать строка «Хаха» и только она. Регулярки являются регистрозависимыми, поэтому строка «хаха» (с маленькой буквы) уже не будет соответствовать выражению выше.",
        "task_description": "Найдите строку «хохо»",
        "text": "Дед мороз увидел мой сюрприз и сказал хохо! Хехе в этом было мало, но было забавно! ",
        "expected_result": "хохо",
    },
    {
        "title": "aa",
        "theory_text": "Однако уже здесь следует быть аккуратным — как и любой язык, регексы имеют спецсимволы, которые нужно экранировать. Вот их список: ^ $ * + ? { } [ ] \\ | ( ). Экранирование осуществляется обычным способом — добавлением \\ перед спецсимволом.",
        "task_description": "Используйте спецсимвол:",
        "text": "Пример текста",
        "expected_result": "pattern",
    },
    {
        "title": "Квантификаторы",
        "theory_text": "Вернёмся к нашему примеру. Что, если в «смеющемся» междометии будет больше одной гласной между буквами «х», например «Хаахаааа»? Наша старая регулярка уже не сможет нам помочь. Здесь нам придётся воспользоваться квантификаторами. Попробуйте Ха{3}ха",
        "task_description": "Хаахаааа",
        "text": "Хаахаааа",
        "expected_result": "Хаахаааа",
    },
    {
        "title": "Скобочные группы",
        "theory_text": "Для нашего шаблона «смеющегося» междометия осталась самая малость — учесть, что буква «х» может встречаться более одного раза, например, «Хахахахааахахооо», а может и вовсе заканчиваться на букве «х». Вероятно, здесь нужно применить квантификатор для группы [аиое]+х, но если мы просто напишем [аиое]х+, то квантификатор + будет относиться только к символу «х», а не ко всему выражению. Чтобы это исправить, выражение нужно взять в круглые скобки: ([аиое]х)+. Таким образом, наше выражение превращается в [Хх]([аиое]х?)+ — сначала идёт заглавная или строчная «х», а потом произвольное ненулевое количество гласных, которые (возможно, но не обязательно) перемежаются одиночными строчными «х». Однако это выражение решает проблему лишь частично — под это выражение попадут и такие строки, как, например, «хихахех» — кто-то может быть так и смеётся, но допущение весьма сомнительное. Очевидно, мы можем использовать набор из всех гласных лишь единожды, а потом должны как-то опираться на результат первого ",
        "task_description": "Выполните задание для закрепления!",
        "text": "Исходный текст Adipisicing porro enim enim libero saepe? Cum sunt illo temporibus incidunt quam Vero doloribus quasi iure magni numquam mollitia! Deserunt quae similique consequatur laboriosam enim Magnam ipsam molestiae harum id",
        "expected_result": "pattern",
    },
    {
        "title": "Задание для закрепления",
        "theory_text": "Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите RegEx выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» — некорректное время.",
        "task_description": "Найдите время",
        "text": "Завтрак в 09:00. Ужин в 37:98",
        "expected_result": "09.00",
    },
    {
        "title": "Задание для закрепления",
        "theory_text": "Итак, нужно написать выражение для описания цвета, который начинается с «#», за которым следуют 6 шестнадцатеричных символов. Шестнадцатеричный символ можно описать с помощью [0-9a-fA-F]. Для его шестикратного повторения мы будем использовать квантификатор {6}.",
        "task_description": "Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.",
        "text": "Бирюзовый цвет: #ABCDEF, розовый цвет: #d3CDEF",
        "expected_result": "#ABCDEF,#d3CDEF",
    },
]
