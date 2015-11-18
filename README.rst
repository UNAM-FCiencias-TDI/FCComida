FCComida
========

.. contents:: :local:

.. image:: https://travis-ci.org/UNAM-FCiencias-TDI/FCComida.svg
    :target: https://travis-ci.org/UNAM-FCiencias-TDI/FCComida

Instalación
-----------

.. code:: bash

    $ virtualenv FCComida
    $ cd FCComimda
    $ source bin/activate
    (FCComida)$ git clone https://github.com/UNAM-FCiencias-TDI/FCComida.git
    (FCComida)$ cd FCComida
    (FCComida)$ pip install -r requirements.txt


Configuración de la base de datos (PostgreSQL)

.. code:: bash

    (FCComida)$ sudo -u postgres createuser -W FCComida
    (FCComida)$ sudo -u postgres createdb FCComida -O FCComida


Ejecución
---------

.. code:: bash

    (FCComida)$ python manage.py migrate
    (FCComida)$ python manage.py createsuperuser
    (FCComida)$ python manage.py runserver
