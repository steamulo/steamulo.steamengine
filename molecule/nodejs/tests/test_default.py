import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_app_running_and_enabled(host):
    app_service = host.service("test_nodejs")
    assert app_service.is_running
    assert app_service.is_enabled


def test_app_listening(host):
    assert host.socket("tcp://0.0.0.0:3300").is_listening


def test_app_response(host):
    resp = host.run("curl localhost:3300").stdout
    assert "Welcome to Express" in resp


def test_storage_subdirectory_file(host):
    protected_upload = host.file("/test_nodejs/storage/protected_upload")
    assert protected_upload.exists


def test_link_file(host):
    protected_upload = host.link("/test_nodejs/project_root/www/upload")
    assert protected_upload.exists
