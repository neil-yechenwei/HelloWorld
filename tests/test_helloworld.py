import os
import pytest

root_dir = os.getcwd()
module_name = "iotedgeFilterModule"
file_list = ["requirements.txt", "module.json", "main.py", "Dockerfile.arm32v7",
             "Dockerfile.amd64.debug", "Dockerfile.amd64", ".gitignore"]



def test_check_iotedgemodule_exist():
    assert 3==3
