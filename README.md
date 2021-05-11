![Build Status](https://github.com/STEAMULO/ansible-role-steamengine/actions/workflows/test.yml/badge.svg?branch=master)

Steamengine
=========

This role provides production grade installation and deployment workflow for nodejs, tomcat, play, springboot and static files.

Role Variables
------------

Here are the main variables that should be set :

```yaml
# Project name. This is also the base path of the project installation and the system user used to manage the project.
# Default is default_project.
steamengine_project_name: "default_project"

# Project type, should be a value in "static", "springboot", "nodejs", "tomcat", "play".
# No default value but mandatory
steamengine_project_type:

# Url of the build that will be deployed.
# No default value and not mandatory. Nothing will be deployed if missing.
steamengine_build_url:

# Checksum of the build. Should be in the following format : "<algorithm>:<checksum>"
# No default value, mandatory if steamengine_build_url is set.
steamengine_build_checksum:

# Project configuration.
# No default value and not mandatory.
steamengine_project_configuration:

# Name of the project default configuration file.
# File content is merged with steamengine_project_configuration variable.
# Variables defined in steamengine_project_configuration override those defined in the base file.
# Used only for tomcat and springboot project type
# No default value and not mandatory.
steamengine_project_configuration_base_name:

# Public ssh keys that will be added to the project user.
# Default is empty.
steamengine_project_ssh_keys: []
```

Example Playbook
------------

Examples for different project types can be found under the molecule folder:
* [Node.js](molecule/nodejs/playbook.yml)
* [Play](molecule/play/playbook.yml)
* [SpringBoot](molecule/springboot/playbook.yml)
* [Static](molecule/static/playbook.yml)
* [Tomcat](molecule/tomcat/playbook.yml) 

Development
------------

This role use the [molecule framework](https://molecule.readthedocs.io/en/stable/) in order to simplify the development process.

Requirements:
* [Python 3](https://www.python.org/download)
* [Docker](https://docs.docker.com/get-docker/)

Setup your local environnement with python virtualenv prior to using molecule : `. venv.sh`

This command will create a virtual env, activate it and download python dependencies.

Use ```molecule converge -s <project_type>``` to create a local environnement and ```molecule login -s <project_type>``` to log into the test machine.

Before any commit ensure that every test are passing with ```molecule test --all```

License
------------

BSD

Author Information
------------

Steamulo - www.steamulo.com
