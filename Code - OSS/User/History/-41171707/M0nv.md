## Installation
```
$ pip install -r requirements.txt
```

## Migrations
```
$ python manage.py makemigrations admin
$ python manage.py migrate admin 
$ python manage.py migrate auth
$ python manage.py migrate sesstions
$ python manage.py makemigrations adminapp
$ python manage.py migrate adminapp
```

## Usage

```
$ python manage.py createsuperuser
$ python manage.py runserver
```



