import os
import sys
from io import StringIO
import simplegeoip.main
import pytest


def test_main_lookup(capsys):
    simplegeoip.main.main(args=["testing", "8.8.8.8"])
    out, _ = capsys.readouterr()
    assert "United States" in out

@pytest.mark.skip()
def test_main_update(capsys):
    simplegeoip.main.main(args=["testing", "update"])        

def test_main_info(capsys):
    simplegeoip.main.main(args=["testing", "info"])
    out, _ = capsys.readouterr()
    assert "Geolite database was last updated" in out