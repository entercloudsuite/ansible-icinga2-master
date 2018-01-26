Ansible Role: Icinga2 Master + Icingaweb2 Dashboard
======================================

[![Build Status](https://travis-ci.org/entercloudsuite/ansible-icinga2-master.svg?branch=master)](https://travis-ci.org/entercloudsuite/ansible-icinga2-master)
[![Galaxy](https://img.shields.io/badge/galaxy-entercloudsuite.icinga2--master-blue.svg?style=flat-square)](https://galaxy.ansible.com/entercloudsuite/ansible-icinga2-master)  

Install Icinga2 Master + Icingaweb2 Dashboard on Ubuntu 14.04 (Trusty) or Ubuntu 16.04 (Xenial)

## Requirements

This role requires Ansible 2.0 or higher.

## Role Variables

The role defines its variables in `defaults/main.yml`:

## Example Playbook

Run with default vars:

    - hosts: all
      roles:
        - { role: ansible-icinga2-master }

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
