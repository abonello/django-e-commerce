# E-Commerce - A Django project

a Django project with many apps.  
An e-commerce project which will:
* allow you to display products for sale, 
* allow your customer to search for and 
* add products to a cart and then 
* pay for the products with a credit or debit card.

**Tutor**: Niel McEwen (Code Institute)


### Learning outcomes
* **Sessions** in Django - allow us to keep track of the 'state' between the site 
and a particular users browser. 
* **Stripe** - a tool for Internet commerce that allows both private individuals 
and businesses to accept payments. You will learn how to integrate it into a django app. 
* **Amazon Web Services** - a subsidiary of amazon.com that provides on-demand 
cloud computing platforms to individuals and companies. You will learn how to 
integrate their simple cloud storage service (**s3**) into your Django project 
and use it to serve your static and media files.


The tutorial is using Django 1.11  
Github is warning against using this version due to vulnerabilities. I will try 
to use version 1.11.15
```bash
sudo pip3 install django==1.11.15
```
Apparently it does not have the vulnerability.

---

## Start


1. Install Django
    ```bash
    $ sudo pip3 install django==1.11.15
    ```
2. Create a Django project
    Call it `ecommerce` and put it at the root level of this directory.
    ```bash 
    $ django-admin startproject ecommerce .
    ```
    This will become important when we get to deploy on Heroku.

3. Update ALLOWED_HOSTS
    In settings.py add cloud 9 as an allowed host.  
    `ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')]`

4. Create alias run
    Create the following alias in `.bash_aliases`:  
    `alias run="python3 manage.py runserver $IP:$C9_PORT"`  
    Restart `.bash_aliases` but running
    ```bash
    . ~/.bash_aliases
    ```
    Now I can run the server just by typeing `run` command in a terminal.

5. Initialise Git
    Start git and include the sqlite files in a gitignore file.
    ```bash 
    $ git init
    Initialized empty Git repository in /home/ubuntu/workspace/.git/
    $ echo -e '*.sqlite3\n__pycache__\n' >> .gitignore
    ```
### Copying the django auth app from previous project.
We can downlod the zip from the github or copy the code straight from there.  
I will be checking the code and possibly update it if necessary.

1. In the root of our project create a new directory called `accounts`.

2. Copy all the files from the accounts app and drag them here.

**NOTE: My Code is very different from the code in github for this tutorial.**

3. Create a templates folder at the top level.
    Copy `base.html`. Copy the registration folder with the templates inside it too.

4. Create a `static` folder in the top level of the project.
    Inside this create a `css` directory ~~and copy the style.css file~~. 
    Actually the file used in this tutorial is called custom.css so I will 
    be renameing it. I am expecting this to be very different from the one I have 
    so will need lots of changes.

5. Wiring this app up.
    In `settings.py`:
    * add `accounts` as INSTALLED_APPS.
    * add AUTHENTICATION_BACKENDS - the code from my previous project is
    ```python 
    AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
    ]
    ```
    This tutorial is using `'accounts.backends.CaseInsensitiveAuth'` instead of 
    `'accounts.backends.EmailAuth'`.

I am getting this error:
```
ImportError at /admin/login/
Module "accounts.backends" does not define a "CaseInsensitiveAuth" attribute/class
```
Up to now we should have login capability.

6. Add MESSAGE_STORAGE
    ```python
    MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
    ```
    This is purely to fix an issue that we have with cloud 9.

7. Make migrations and migrate.
    ``bash
    (master) $ python3 manage.py makemigrations
    No changes detected
    ```
    We can do makemigrations for a specific app 
    ``bash
    (master) $ python3 manage.py makemigrations accounts
    No changes detected in app 'accounts'
    ```
    Both cases has no changes detected and that's simply because all your login 
    logout are built in Django functions. If we do a migrate we can see that all 
    those auth tables are built. 

    ```bash 
    (master) $ python3 manage.py migrate
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
    ```
    
8. Tie up some urls
    In `ecommerce/urls.py`, add include function and urls from accounts. Then
    add the url pattern for accounts.
    ```python 
    from django.conf.urls import url, include
    from django.contrib import admin
    from accounts import urls as urls_accounts
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^accounts/', include(urls_accounts)),
    ]
    ```

9. Install django bootstrap for forms
    ```bash 
    (master) $ sudo pip3 install django-forms-bootstrap
    ```

10. Create superuser
    ```bash 
    (master) $ python3 manage.py createsuperuser
    Username (leave blank to use 'ubuntu'): admin
    Email address: admin@test.com
    Password: 
    Password (again): 
    Superuser created successfully.
    ```

11. Add django forms bootstrap in INSTALLED_APPS
    In `settings.py` add django forms bootstrap in `INSTALLED_APPS`
    ```python 
    INSTALLED_APPS = [
        . . .
        'django_forms_bootstrap',
        . . .
    ]
    ```

12. Since we have multiple templates folder we have to specify in our settings 
that all directories called `templates` can contain templates.
    ```
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ```
    In this way we can keep separate templates for each app.

### Replacing `Accounts` app

The code that I am using, the one developed during the previous module is 
different thatn the one used in this tutorial. For this reason I will be 
replacing it with a version that matches this tutorial.
This can be found at [proposed django authentication](https://github.com/Code-Institute-Solutions/proposed_django_authentication/tree/master/accounts).
I forked this and also downloaded the zip file as it will be easier to transfer 
to cloud9. I will keep a copy of the older app and rename the folders by adding 
`1` to the name. The steps to follow are the same as above. Although not all the 
steps will be necessary.

READ the following steps in conjuction with what happened in the previous steps.

1. Rename the `accounts` folder in the root of our project to `accounts1` and 
    create a new directory called `accounts`. 

2. Copy all the files from the new accounts app and drag them here.

3. Rename `base.html` to `base1.html`. Then copy `base.html`. Rename the 
    `registration` forlder to `registration1`. Then copy the `registration` folder with the templates inside it too.

4. In the `css` folder inside the `static` rename `custom.css` to `custom1.css`. 
    Then copy `custom.css` from the new app.

5. Wiring this app up.
    In `settings.py`:
    * ~~add `accounts` as INSTALLED_APPS.~~ This is already done.
    * add AUTHENTICATION_BACKENDS - ~~the code from my previous project is~~
    ```python 
    AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
    ]
    ```
    Change `'accounts.backends.EmailAuth'` for `'accounts.backends.CaseInsensitiveAuth'`.


6. ~~Add MESSAGE_STORAGE~~ - NO CHANGES HERE

7. ~~Make migrations and migrate~~. - NO CHANGES HERE
    I tried to the `makemigrations` and `makemigrations accounts`. Both came with 
`No changes detected` as I expected. I also checked the migrate and confirmed that 
there are `No migrations to apply`.
    
8. ~~Tie up some urls~~. - NO CHANGES HERE
    There are no changes needed in `ecommerce/urls.py`.

9. ~~Install django bootstrap for forms~~. - NO CHANGES HERE

10. ~~Create superuser~~. - NO CHANGES HERE

11. ~~Add django forms bootstrap in INSTALLED_APPS~~. - NO CHANGES HERE

12. ~~Template directories~~. - NO CHANGES HERE


---
## It looks like I am in synch with the tutorial now.

As at the end of  
[Course  > Putting It All Together | ECommerce Mini Project  > 
Products and a Shopping Cart   > Reusing an accounts app](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+F101+2017_T1/courseware/c95cdb47b7bb40e49bbfb75cb4c29114/01fbdaedba5d4db19ad118cbe07c1ab7/?activate_block_id=block-v1%3ACodeInstitute%2BF101%2B2017_T1%2Btype%40sequential%2Bblock%4001fbdaedba5d4db19ad118cbe07c1ab7)
---
