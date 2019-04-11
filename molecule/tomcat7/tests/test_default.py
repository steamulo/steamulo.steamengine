import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_app_running_and_enabled(host):
    app_service = host.service("test_tomcat7")
    assert app_service.is_running
    assert app_service.is_enabled


def test_app_listening(host):
    assert host.socket("tcp://0.0.0.0:8088").is_listening


def test_app_response(host):
    resp = host.run("curl localhost:8088/hello").stdout
    assert "the Hello, World application" in resp


def test_configuration_file(host):
    conf = host.file("/test_tomcat7/conf/project_env.conf").content_string
    assert "test_conf.item1=test1" in conf
    assert "test_conf.item2.item2_sub1=test2" in conf
    assert "test_conf.item2.item2_sub2=test3" in conf
