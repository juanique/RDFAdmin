
# RDFAdmin

## Ubuntu quickstart

1.  It will install Django 1.3, Django-pistons 0.2.2, as well as mechanize, beautifulsoup and setuptools using apt-get.

    #Clone the git repo
    git clone https://github.com/juanique99/RDFAdmin.git RDFAdmin
    cd RDFAdmin

    #Install dependencies
    ./dependencies.sh

    #Create local settings, edit the file as necessary.
    cp local_settings.py.example local_settings.py

    #Run the server
    python manage.py runserver

2. Open http://localhost:8000/ on your web browser.

## Getting started

1. You may need to install Python 2.6, Django and other Python
   libs. See the requirements section to see how to install them.

2. Get the code

    git clone https://github.com/juanique99/RDFAdmin.git

3. Copy +local_settings.py.example+ to +local_settings.py+ and edit it
   according to your local config. In particular, make sure to set your 
   Virtuoso access variables.

3.3 If using a DB diferent that the default in memory sqlite3, make sure to create the app tables
    
    python manage.py syncdb

5. Run with

    python manage.py runserver

## Using apache2

0. You will need to install apache2 mod wsgi library

    sudo apt-get install libapache2-mod-wsgi

1. Update your apache configuration (in ubuntu /etc/apache2/sites-enabled/default).
Change the appropiate path for the djang.wsgi file at the root of the project.

    <VirtualHost *>
        WSGIScriptAlias / /home/user/RDFAdmin/django.wsgi

        <Directory /home/user/RDFAdmin>
            Order allow,deny
            allow from all
        </Directory>
    </VirtualHost>


2. Setup your support database. It is not recomended to use the default in-memory database
When using apache. A simple example for the local settings using sqlite3 would be

    DATABASES = {
        'file': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/rdfadmin.sqlite3', #Make sure apache can read/write to this file
        }
    }

3. Create database tables.

    python manage.py syncdb

## System requirements

- Python 2.6
- Django 1.3

### Installation

0. If you don't have the Virtuoso triple store yet, install it

    sudo apt-get install virtuoso-opensource-6.1

1. Install Django

   Django 1.3 isn't as a package in current distributions of
   Debian/Ubuntu, so yo must install it using the tarball.

    wget http://www.djangoproject.com/download/1.3/tarball/
    tar xzvf Django-1.3.tar.gz
    cd Django-1.3
    sudo python setup.py install
    
2. Install Django pistons

    wget http://bitbucket.org/jespern/django-piston/downloads/django-piston-0.2.2.tar.gz
    tar -xvzf django-piston-0.2.2.tar.gz
    cd django-piston
    sudo python setup.py install

3. Install Beatiful Soup and Mechanize

   This packages are in current Debian/Ubuntu distributions so you can
   install them using the package manager.
   
    sudo apt-get install python-beautifulsoup python-mechanize

4. Edit /etc/virtuoso-opensource-6.0/virtuoso.ini and add the settings.VIRTUOSO_WORK_DIR to the DirsAllowed variable, you can use the following command which will add the PROJECTPATH/data/ subdirectories to the virtuoso.ini DirsAllowed variable. 

    reset.sh virtuoso-autoset-dir

5. If using the php proxy for sparql queries (optional)

    sudo apt-get install php5-curl


### Database setup

RDFAdmin uses a relational database to save session data and indices. The default settings in local_settings.py 
use a simple sqlite3 file. But you can use any database engine supported by Django (See Djando documentation).

