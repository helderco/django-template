# {{ cookiecutter.project_name }}

## Requirements

Docker Compose!

## Usage

    $ docker-compose up -d
    $ docker run -it --rm -u node -v "$PWD/src:/data" helder/node bower install
    $ docker-compose run --rm manage check
    $ docker-compose run --rm manage migrate
    $ docker-compose run --rm manage createsuperuser
    $ docker-compose run --rm manage collectstatic
