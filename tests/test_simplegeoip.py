import os
import simplegeoip
import pytest


def test_lookup():
    d = simplegeoip.lookup("8.8.8.8")
    assert d["country"]["iso_code"] == "US"

def test_lookup_no_ip():
    with pytest.raises(Exception):
        d = simplegeoip.lookup("notanip")
    
@pytest.mark.skip()
def test_download():
    p = simplegeoip.database_path()
    os.unlink(p)
    assert not os.path.exists(p)
    simplegeoip.download_latest_database_from_maxmind()
    test_lookup()

def test_latest_update():
    assert "Geolite database was last updated" in simplegeoip.last_updated()

