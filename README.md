### Virtual Environment
```shell
pip install virtualenv
virtualenv env
```

### Django Installation and Version
```shell
pip install django
python -m django --version
```

```python
import django
print("djagno Version: " + django.get_version())
```

### Create Application
```shell
django-admin
django-admin startapp home
```

### Run HTTP Server
```shell
python manage.py runserver
```