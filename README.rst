FCComida
========

.. contents:: :local:

.. image:: https://travis-ci.org/UNAM-FCiencias-TDI/FCComida.svg
    :target: https://travis-ci.org/UNAM-FCiencias-TDI/FCComida

Instalación
-----------

.. code:: bash

    $ virtualenv FCComida
    $ source bin/activate
    (FCComida)$ git clone https://github.com/UNAM-FCiencias-TDI/FCComida.git
    (FCComida)$ cd FCComida
    (FCComida)$ pip install -r requirements.txt


Configuración de la base de datos (PostgreSQL)

.. code:: bash
	
<<<<<<< HEAD
	$ sudo -u postgres createuser -W FCComida
	$ sudo -u postgres createdb FCComida -O FCComida
    (fcsocial_dev)$ python manage.py migrate
    (fcsocial_dev)$ python manage.py createsuperuser
=======
	(FCComida)$ sudo -u postgres createuser -W FCComida
	(FCComida)$ sudo -u postgrescreatedb FCComida -O FCComida
    (FCComida)$ python manage.py migrate
    (FCComida)$ python manage.py createsuperuser
>>>>>>> bf9f6b741f3fcfe28ed705162f28b5b0114befac

Ejecución
---------

.. code:: bash

    (FCComida)$ python manage.py runserver
