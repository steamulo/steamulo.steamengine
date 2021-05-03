import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_app_nginx_running_and_enabled(host):
    app_service = host.service("nginx")
    assert app_service.is_running
    assert app_service.is_enabled


def test_app_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_drupal8_drush_install_index_page(host):
    resp = host.run("curl --resolve 'drupal8-drush-install.test:80:127.0.0.1' http://drupal8-drush-install.test/").stdout
    assert '<a href="/" title="Accueil" rel="home">drupal</a>' in resp


def test_drupal8_db_dump_index_page(host):
    resp = host.run("curl --resolve 'drupal8-db-dump.test:80:127.0.0.1' http://drupal8-db-dump.test/").stdout
    assert '<a href="/" title="Accueil" rel="home">drupal</a>' in resp


def test_drupal9_drush_install_index_page(host):
    resp = host.run("curl --resolve 'drupal9-drush-install.test:80:127.0.0.1' http://drupal9-drush-install.test/").stdout
    assert '<a href="/" title="Accueil" rel="home">drupal</a>' in resp


def test_drupal9_db_dump_index_page(host):
    resp = host.run("curl --resolve 'drupal9-db-dump.test:80:127.0.0.1' http://drupal9-db-dump.test/").stdout
    assert '<a href="/" title="Accueil" rel="home">drupal</a>' in resp
