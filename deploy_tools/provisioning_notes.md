Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.6
* virtualenv + pip
* Git

sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config
* see nginx.template.conf
* replace DOMAIN with e.g. staging.example.com

## Systemd service
 * see gunicorn-systemd.template.service
 * replace DOMAIN with e.g. staging.example.com

## Folder structure:
Assume we have a user account /home/username

/home/username
  -- sites
      DOMAIN1
        .env
        db.sqlite3
        manage.py etc
        static
        virtualenv
      DOMAIN2
        .env
        db.sqlite3
        etc