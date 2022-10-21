Template
=========

This role acts as a template for my other roles. Feel free to use it yourself. The tasks are split into two parts. There is an 'install' and a 'configure' part.

The install part handles the installation of packages, the creation of users and groups and the installation of the systemd service file. The configure part handles the creation of the needed configuration files and ensures the service is in the right startup and running state.

Requirements
------------

This role has no additional requirements.

Role Variables
--------------

| Variable | Default | Description |
| -------- | ------- | ----------- |
| template_enabled | yes | Controls whenever the template service should be running and started at boot |
| template_config_dir | `"/etc/template"` | The directory to put the configuration file in |
| template_script_path | `"/usr/local/bin/template"` | The path where the template script is installed |
| template_user | `"template"` | The user that the service should run under |
| template_group | `"template"` | The group that the service should run under |
| template_service | `"template"` | The name of the service |
| template_package | `"sl"` | The name of the package to install |

Role Tags
---------

| Tag | Description |
| --- | ----------- |
| template-install | Runs installation tasks such as installing packages, creating users and groups and installing service files |
| template-configure | Runs configuration tasks such as creating configuration directories and files |
| template-validate | Runs tasks that validate the variables and system configuration and ensures that the role can be properly deployed |
| install | Global install tag. Allows you to easily run the installation tasks on a multitude of compatible roles |
| configure | Global configure tag. Allows you to easily run the configuration tasks on a multitude of compatible roles |
| validate | Global validate tag. Allows you to easily run the validation tasks on a multitude of compatible roles |

Dependencies
------------

This role has no dependencies.

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - vharmers.template
  vars:
    template_enabled: no  # Install and configure but don't start the service yet
    template_config_dir: "/etc/foo"
    template_package: vim
```

Testing
-------

Testing is done with [Molecule](https://molecule.readthedocs.io/en/latest/) and [Vagrant](https://www.vagrantup.com).

**Step 1:** Install a hypervisor such as [VirtualBox](https://www.virtualbox.org).

**Step 2:** Install Vagrant. Follow the installation instructions for your OS on the [downloads](https://www.vagrantup.com/downloads) page.

**Step 3:** Install the necessary Python packages:

```bash
pip install ansible ansible-lint molecule molecule_vagrant pytest-testinfra
```

**Step 4:** Descent into the role directory and run the `molecule test` command.

License
-------

[Unlicense](LICENSE)

Author Information
------------------

*Valentijn Harmers* ([website](https://www.vharmers.com))
