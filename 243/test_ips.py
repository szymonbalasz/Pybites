import os
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network('192.0.2.8/29')


@pytest.fixture(scope='module')
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH

# write your pytest code ...


@pytest.mark.parametrize("arg, expected", [
    ("13.248.118.0", "13.248.118.0/24 is allocated to the AMAZON service in the eu-west-1 region")
])
def test_correct(json_file, arg, expected):
    actual = str(get_aws_service_range(
        arg, parse_ipv4_service_ranges(json_file))[0])
    assert actual == expected


@pytest.mark.parametrize("err_arg", [
    ("13.248.118.0.5"),
    ("1313.248.118.0"),
    ("13.266.118.0"),
    ("hello"),
    ("7"),
    ("True"),
    ("")
])
def test_err(json_file, err_arg):
    with pytest.raises(ValueError, match="Address must be a valid IPv4 address"):
        get_aws_service_range(err_arg, parse_ipv4_service_ranges(json_file))
