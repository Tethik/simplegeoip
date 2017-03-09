import os
import simplegeoip
import pytest


def test_lookup():
    d = simplegeoip.lookup("8.8.8.8")
    assert d["country"]["iso_code"] == "US"

def test_lookup_no_ip():
    with pytest.raises(Exception):
        d = simplegeoip.lookup("notanip")
    
@pytest.mark.skipif("TRAVIS" not in os.environ, reason="Skip so that we don't spam the somewhat heavy download.")
def test_download():
    p = simplegeoip.database_path()
    os.unlink(p)
    assert not os.path.exists(p)
    simplegeoip.download_latest_database_from_maxmind()
    test_lookup()

def test_latest_update():
    assert "Geolite database was last updated" in simplegeoip.last_updated()

def test_reader():
    # # Not supported yet by maxminddb
    # with simplegeoip.reader() as reader:
    #     reader.get('8.8.8.8')
    #     assert d["country"]["iso_code"] == "US"

    r = simplegeoip.reader()
    assert r.get('8.8.8.8')["country"]["iso_code"] == "US"
    r.close()
    

