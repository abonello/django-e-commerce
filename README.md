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
