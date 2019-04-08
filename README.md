# django_todoList_app
Todo list app using django

1. install virtualenv
pip install virtualenv

2. start virtualenv
virtualenv .

3. check list of virtualenv
ls

4. activate virtualenv
.\Scripts\activate

5.install django on virtualenv
pip install django

6.check list
pip freeze 
pip freeze > requirements.txt
pip install -r requirements.txt

7. now create new app
django-admin.py startproject todo
cd todo 
todo dir has manage.py 

8. start the servive
python manage.py runserver

9. u'll get navigation url
http://127.0.0.1:8000/

10. now run new powershell and run virtualenv again using step 4 in your directory
cd ToDoListApp 
.\Scripts\activate
cd todolist\todo 

11. now fix migration errors
python manage.py migrate 

12. create main app now 
python manage.py startapp todo_list

13.go to the editor with following path
cd ToDoListApp\todolist\todo\todo

14. register the main app in original app
open settings.py
installed_apps = 'todo_list'

15. in todo_list create a new file name urls.py 

16. open original urls.py from cd ToDoListApp\todolist\todo\todo
few changes in this file 

17. create template folder in todo_list
add home.html in that folder

18. open views.py in todo_list and add changes


