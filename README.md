# Django-friends-service

Создание Django проекта  
$ django-admin startproject service   
$ cd service   
Создание приложения    
$ python3 manage.py startapp app

Вместо появившиься файлов в папке app вставляем файлы models.py, views.py и добавляем serializers.py и меняем папку urls.py в папке service

В папке service в файл settings.py в INSTALLED APS добавляем   
'app.apps.AppConfig',  
'rest_framework',  

После внесенных изменений запускаем сервер  
$ python3 manage.py makemigrations  
$ python3 manage.py migrate  
$ python3 manage.py runserver  

После чего должны увидеть следующее сообщение в консоли  
Watching for file changes with StatReloader  
Performing system checks...  
  
System check identified no issues (0 silenced).  
May 10, 2023 - 14:21:54  
Django version 3.2.12, using settings 'service.settings'  
Starting development server at http://127.0.0.1:8000/  
Quit the server with CONTROL-C.  
  
Чтобы убедится что все работает правильно, создадим пользователя.  
Для этого воспользуемя POST запросом с использованием curl:  
curl -X POST -H "Content-Type: application/json" -d '{"username": "alex"}' http://localhost:8000/users/  
или $ http POST http://localhost:8000/users/ username=alex  
или перейдем на страницу http://localhost:8000/users/ в браузере и добавим пользователя.  
  
После чего получим в консоли вот такой ответ [10/May/2023 14:22:36] "POST /users/ HTTP/1.1" 201 12025  
или   
HTTP 201 Created  
Allow: POST, OPTIONS  
Content-Type: application/json  
Vary: Accept  
  
{  
"id": 1,  
"username": "alex"  
}  
  
в веб браузере.  
