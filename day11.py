amal@amal-System-Product-Name:~$ cd Documents
amal@amal-System-Product-Name:~/Documents$ source spect_env/bin/activate
(spect_env) amal@amal-System-Product-Name:~/Documents$ django-admin startproject e_shop
CommandError: '/home/amal/Documents/e_shop' already exists
(spect_env) amal@amal-System-Product-Name:~/Documents$ django-admin startproject e_shop1
(spect_env) amal@amal-System-Product-Name:~/Documents$ cd e_shop1
(spect_env) amal@amal-System-Product-Name:~/Documents/e_shop1$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

April 28, 2021 - 15:26:53
Django version 1.11.29, using settings 'e_shop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
python manage.py migrate
^C(spect_env) amal@amal-System-Product-Name:~/Documents/e_shop1$ python manage.pnserver
python: can't open file 'manage.pyunserver': [Errno 2] No such file or directory
(spect_env) amal@amal-System-Product-Name:~/Documents/e_shop1$ python manage.y migrate
python: can't open file 'manage.y': [Errno 2] No such file or directory
(spect_env) amal@amal-System-Product-Name:~/Documents/e_shop1$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
(spect_env) amal@amal-System-Product-Name:~/Documents/e_shop1$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 28, 2021 - 15:34:13
Django version 1.11.29, using settings 'e_shop1.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[28/Apr/2021 15:34:49] "GET / HTTP/1.1" 200 1716

