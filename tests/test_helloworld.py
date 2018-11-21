import os
import pytest
import re

VALID_DEVICECONNECTIONSTRING = os.environ['DEVICE_CONNECTION_STRING']


def test_check_iotedgemodule_exist():
    os.environ
    device_id = re.findall(
        ".*DeviceId=(.*);SharedAccessKey.*", VALID_DEVICECONNECTIONSTRING)[0]
    print(device_id)
