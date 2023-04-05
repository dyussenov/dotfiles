# Работа с DOM при помощи JavaScript

## Атрибут ```onclick```

В качестве основы возьмем страницу с кнопкой ```btn```, при нажатии на которую будет меняться  блок ```change```:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>JS test</title>
</head>
<body>
    <div class="btn">
        Press me!
    </div>
    <div class="change">
        Change me!
    </div>
</body>
</html>
<style>
    .btn{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
        margin-bottom: 5px;
        width: 100px;
        background-color: #1bca96;
        color: white;
        cursor: pointer;
    }
    .change{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 300px;
        height: 300px;
        background-color: #5b5d63;
    }
</style>
```

Один из способов совершать действия при нажатии на элемент - указать атрибут ```onclick``` в элементе, по которому будет производиться нажатие. В качестве значения этого атрибута определим JS функцию:

