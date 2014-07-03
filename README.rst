
::

    cd source/theme
    bundle install
    bower install
    cd ../..

    foreman start

.. code-block:: bash

    alias start-django="django-admin.py startproject --template=https://github.com/helderco/django-template.git -e py,ruby-gemset,json,env"
