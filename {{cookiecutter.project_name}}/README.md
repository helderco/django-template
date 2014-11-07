# What's in {{ cookiecutter.project_name }}?

* Django 1.7
* bower: for javascript dependencies;
* bundler: for ruby dependencies, i.e, compass/sass, foreman (use RVM);
* compass: for compiling CSS;
* foreman: for running several processes in one terminal window.

Tweak `settings/base.py`, then on first run:

    $ pip install -r req/dev.txt
    $ cd src/core
    $ bundle install
    $ bower install
    $ cd ..
    $ ./manage.py check
    $ ./manage.py migrate

After that

    $ foreman start
