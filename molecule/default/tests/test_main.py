
def test_installed(host):
    package = host.package("sl")
    assert package.is_installed


def test_config(host):
    config = host.file("/etc/template/template.conf")
    assert config.user == "template"
    assert config.group == "template"
    assert config.mode == 0o644


def test_service(host):
    service = host.service("template")
    assert service.is_running
    assert service.is_enabled
