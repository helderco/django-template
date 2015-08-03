# {{ cookiecutter.project_name }}

## Requirements

Docker Compose!

## Useful aliases

    alias drun="docker run -it --rm"
    alias dc="docker-compose"
    alias dc-run="dc run --rm"
    alias dc-db="dc-run db mysql -uroot -proot -hdb"

    alias bower='drun -u node -v "$PWD:/data" helder/node bower'

    function docker-host {
      type docker-machine >/dev/null 2>&1 && docker-machine ip $DOCKER_MACHINE_NAME || \
        ifconfig | sed -En 's/.*inet (addr:)?(192.168(\.[0-9]*){2}).*/\2/p' | head -n1
    }

    function dc-port {
        echo `docker-compose port $1 $2 | cut -d: -f2`
    }

    function dc-open {
        open http://`docker-host`:`dc-port ${1:-web} ${2:-80}`$3
    }

## Usage

    $ dc up -d
    $ (cd src && bower install)
    $ dc-run manage check
    $ dc-run manage migrate
    $ dc-run manage createsuperuser

    # Prod
    $ dc-run manage collectstatic
    $ dc-open

    # Dev
    $ dc-open manage

    # Captured emails
    $ dc-open mail
