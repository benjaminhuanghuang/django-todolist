## Add url
    change proj/urls.py
    add urls.py in app
    add url-view mapping app/urls.py 


## View
    from django.shortcuts import render
    from django.http import HttpResponse

## Add Models and table
### Create model    
    class Todo(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        created = models.DateTimeField(default=datetime.now, blank=True)

### make migration for the model
    $ python manage.py makemigrations todos

### check migration script
    $ python manage.py sqlmigrate todos 0001

### migrate, create table in db for the model
    $ python manage.py migrate




