import os
import sys
from io import StringIO
import simplegeoip.main
import pytest

def test_main_helptext(capsys):
    simplegeoip.main.main(args=["testing"])
    out, _ = capsys.readouterr()
    assert "USAGE" in out

def test_main_lookup(capsys):
    simplegeoip.main.main(args=["testing", "8.8.8.8"])
    out, _ = capsys.readouterr()
    assert "United States" in out

def test_main_lookup_noresult(capsys):
    simplegeoip.main.main(args=["testing", "127.0.0.1"])
    out, _ = capsys.readouterr()
    assert "Nothing found" in out

def test_main_lookup_err(capsys):
    simplegeoip.main.main(args=["testing", "bad"])
    out, _ = capsys.readouterr()
    assert "does not appear to be an IPv4" in out

@pytest.mark.skipif("TRAVIS" not in os.environ, reason="Skip so that we don't spam the somewhat heavy download.")
def test_main_update(capsys):
    simplegeoip.main.main(args=["testing", "update"])        

def test_main_info(capsys):
    simplegeoip.main.main(args=["testing", "info"])
    out, _ = capsys.readouterr()
    assert "Geolite database was last updated" in out