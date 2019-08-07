GIT Initialization:
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/SiGnaLz314/FatStackPy_Web.git
    git push -u origin master
GIT Commit/Push
    git add .
    git commit "  COMMENT  "
    git push -u origin master
    
TEST Setup:
    python manage.py runserver

ADD APP:
    python manage.py startapp <APP NAME>

ADD URLS:
    Add urls.py to /<APP NAME> directory
    
settings.py
    ADD:
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    POSTGRESQL:
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'FatStackPyWeb',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
            }
        }
    
MIGRATE to create necessary admin tables in the db:
    python manage.py migrate
    
MODELS define data you will be storing:
    /<APP NAME>/models.py

MIGRATE MODELS:
    python manage.py makemigrations <APP NAME>
    python manage.py sqlmigrate polls <MIGRATION NUMBER>
    python manage.py migrate
    
API Query Database:
    python manage.py shell
    

Django Admin:
    Create SuperUser:
        python manage.py createsuperuser
        Username: admin
        EmailAddress: <EMAIL>
        Password: <PASS>
        
        python manage.py runserver
        
        http://127.0.0.1:8000/admin

<APP NAME> ADMIN:
    from django.contrib import admin
    from .models import <MODEL NAME>
    
    admin.site.register(<MODEL NAME>)
    
