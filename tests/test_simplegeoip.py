import os
import pytest
import simplegeoip


def test_lookup():
    result = simplegeoip.lookup("8.8.8.8")
    assert result["country"]["iso_code"] == "US"

def test_lookup_no_ip():
    with pytest.raises(Exception):
        simplegeoip.lookup("notanip")

@pytest.mark.skipif("TRAVIS" not in os.environ,
                    reason="Skip so that we don't spam the somewhat heavy download.")
def test_download():
    path = simplegeoip.database_path()
    os.unlink(path)
    assert not os.path.exists(path)
    simplegeoip.download_latest_database()
    test_lookup()

def test_database_path_no_dir(monkeypatch):
    def _mockreturn(_):
        return None
    monkeypatch.setattr(simplegeoip, '_ensure_dir_exists', _mockreturn)
    monkeypatch.setattr(simplegeoip, '_ensure_dir_exists', _mockreturn)
    with pytest.raises(EnvironmentError):
        simplegeoip.database_path()

def test_latest_update():
    assert "Geolite database was last updated" in simplegeoip.last_updated()

def test_reader():
    with simplegeoip.reader() as reader:
        result = reader.get('8.8.8.8')
        assert result["country"]["iso_code"] == "US"

    result = simplegeoip.reader()
    assert result.get('8.8.8.8')["country"]["iso_code"] == "US"
    result.close()

