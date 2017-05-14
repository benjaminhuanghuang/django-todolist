## Django use sqlite3 by default
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
        
## Use mysql
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "todolist",
            'USER': "root",
            'PASSWORD': "root",
            'HOST': '127.0.0.1',
            'PORT': '3306'
        }
    }   

    $ brew install mysql  # install mysql connector lib
    $ pip install python-mysqldb   # python 2.7

## migration
    $ python manage.py migrate