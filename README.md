Steamengine
=========

This role provides production grade installation and deployment workflow for nodejs, tomcat7, springboot and static files.

Role Variables
--------------

Here are the main variables that should be set :

```yaml
# Project name. This is also the base path of the project installation and the system user used to manage the project.
# Default is default_project.
steamengine_project_name: "default_project"

# Project type, should be a value in "static", "springboot", "nodejs", "tomcat7".
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

# Public ssh keys that will be added to the project user.
# Default is empty.
steamengine_project_ssh_keys: []
```

Example Playbook
----------------

Examples for different project types can be found under the molecule folder.

Development
------------

This role use the [molecule framework](https://molecule.readthedocs.io/en/stable/) in order to simplify
the development process.

Setup your local environnement with python virtualenv prior to using molecule :

```virtualenv ~/.virtualenv/steamengine && source ~/.virtualenv/steamengine/bin/activate && pip install -r requirements.txt```

Use the commande ```molecule converge -s <project_type>``` to create a local environnement
ans ```molecule login -s <project_type``` to log into the test machine.

Before any commit ensure that every test are passing with ```molecule test --all```

License
-------

BSD

Author Information
------------------

Steamulo - http://www.steamulo.com