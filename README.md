Ansible Role: Icinga2 Master + Icingaweb2 Dashboard
======================================

[![Build Status](https://travis-ci.org/entercloudsuite/ansible-icinga2-master.svg?branch=master)](https://travis-ci.org/entercloudsuite/ansible-icinga2-master)
[![Galaxy](https://img.shields.io/badge/galaxy-entercloudsuite.icinga2--master-blue.svg?style=flat-square)](https://galaxy.ansible.com/entercloudsuite/icinga2-master)  

Install Icinga2 Master + Icingaweb2 Dashboard on Ubuntu 14.04 (Trusty) or Ubuntu 16.04 (Xenial)

## Requirements

This role requires Ansible 2.3 or higher.

## Role Variables

The role defines its variables in `defaults/main.yml`:

## Varibles definitition

### GENERAL
|VARIABLE|DESCRIPTION|DEFAULT VALUE|
|--------|-----------|-------------|
|server_timezone|Server timezone|UTC|
|environment_name|Name of infrastructure to monitor|myinfra|
|monitoring_domain|Domain of infrastructure|mydomain.com| 
|fqdn_local_mailserver|FQDN for mail source host|

### DATABASE
|VARIABLE|DESCRIPTION|DEFAULT VALUE|
|--------|-----------|-------------|
|mysql_root_password|Root password for mysql backend|mysqlrootpassword|
|icinga2_mysql_database|Database name for icinga2 server|icinga2|
|icinga2_mysql_user|Database username for icinga2 server|icinga2|
|icinga2_mysql_password|Database password for icinga2 server|icinga2|
|icingaweb2_mysql_database|Database name for icinga2 dashboard|icinga2|
|icingaweb2_mysql_user|Database username for icinga2 dashboard|icinga2|
|icingaweb2_mysql_password|Database password for icinga2 dashboard|icinga2|

### ICINGA2
|VARIABLE|DESCRIPTION|DEFAULT VALUE|
|--------|-----------|-------------|
|icinga2_api_root_password|Icinga2 internal root privileged API secret|apirootsecret|
|icinga2_api_admin_user|Icinga2 dashboard internal API username|admin|
|icinga2_api_admin_password|Icinga2 dashboard internal API password|adminsecret|
|icinga2_master_host|Icinga2 ansible host (use ansible group or IP/hostname used into inventory)|{{ groups['icinga2-master'][0] }} or 127.0.0.1|
|--------|-----------|-------------|
|icinga2_host_notification_period|Period of alert notification for hosts|3600|
|icinga2_service_notification_period|Period of alert notification for services|3600|
|icinga2_notification_users (Multi value)|List of email user for notification|-|
|-|user|icingaadmin|
|-|name|Icinga Administrator|
|-|email|root@localhost|
|--------|-----------|-------------|
|(Optional) icinga2_notification_telegram (Multi value)|List of telegram user for notification|-|
|-|name|Icinga Telegram|
|-|chat_id|111111111|
|-|bot_token|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|

### ICINGA2 OPTIONAL HOST/SERVICE CHECK
|VARIABLE|DESCRIPTION|DEFAULT VALUE|
|--------|-----------|-------------|
|icinga2_host_url_check (Multi value)|List of web url to check per webserver group|-|
|-|url|www.example.com|
|-|path|/index.html|
|-|ansible_group|webserver|
|--------|-----------|-------------|
|icinga2_host_mysql_check (Multi value)|List of mysql server to check per database group|-|
|-|mysql_username|mysql-user|
|-|mysql_password|password|
|-|group|database|
|--------|-----------|-------------|
|icinga2_host_elasticsearch_check (Multi value)|List of elasticsearch server to check per elasticsearch group|-|
|-|es_port|9200|
|-|group|elasticsearch|
|--------|-----------|-------------|

### ICINGAWEB2
|VARIABLE|DESCRIPTION|DEFAULT VALUE|
|--------|-----------|-------------|
|icingaweb2_dashboard_user|Icinga2 dashboard default user|admin|
|icingaweb2_dashboard_password|Icinga2 dashboard default password|admin|


## Example Playbook

Run with default vars:

    ---

    - name: install icinga2 master
      hosts: icinga2_master
      tags: master
      roles:
        - role: ansible-icinga2-master
          tags: master
      vars:
        - server_timezone: "UTC"
        - environment_name: "example"
        - monitoring_domain: "example.com"
        - icinga2_mysql_password: "password"
        - icingaweb2_mysql_password: "password"
        - icingaweb2_dashboard_user: "admin"
        - icingaweb2_dashboard_password: "password"
        - icinga2_api_root_password: "password"
        - icinga2_api_admin_password: "password"
        - icinga2_api_ticket_salt: "23930b9fadc9bfddbb4fe5875f5f6f2f"
        - icinga2_master_host: "localhost"
        - icinga2_host_notification_period: "3600"
        - icinga2_service_notification_period: "3600"
        - icinga2_notification_users:
            - user: "icingaadmin"
              name: "Icinga Admin"
              email: "root@localhost"

## Testing

Tests are performed using [Molecule](http://molecule.readthedocs.org/en/latest/).

Install Molecule or use `docker-compose run --rm molecule` to run a local Docker container, based on the [enterclousuite/molecule](https://hub.docker.com/r/fminzoni/molecule/) project, from where you can use `molecule`.

1. Run `molecule create` to start the target Docker container on your local engine.  
2. Use `molecule login` to log in to the running container.  
3. Edit the role files.  
4. Add other required roles (external) in the molecule/default/requirements.yml file.  
5. Edit the molecule/default/playbook.yml.  
6. Define infra tests under the molecule/default/tests folder using the goos verifier.  
7. When ready, use `molecule converge` to run the Ansible Playbook and `molecule verify` to execute the test suite.  
Note that the converge process starts performing a syntax check of the role.  
Destroy the Docker container with the command `molecule destroy`.   

To run all the steps with just one command, run `molecule test`. 

In order to run the role targeting a VM, use the playbook_deploy.yml file for example with the following command: `ansible-playbook ansible-icinga2-master/molecule/default/playbook_deploy.yml -i VM_IP_OR_FQDN, -u ubuntu --private-key private.pem`.  

## License

MIT
