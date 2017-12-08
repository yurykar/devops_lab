import sys
import subprocess
import json
import yaml

#version
python_vers = subprocess.getoutput("python --version")
#python executable location
python_ex_l = sys.executable
#python PYTHONPATH
python_path = sys.exec_prefix
#installed packages:
python_pack = subprocess.getoutput("sudo pip freeze").split('\n')
#virtual environment name
pyenv_name = subprocess.getoutput("pyenv version-name")
#pip location
pip_l = subprocess.getoutput("which pip")
#site-packages location


def get_site_package(num):
    for i in range(num):
        if "site-package" in sys.path[i]:
            return sys.path[i]

pack_loc = get_site_package(len(sys.path))

output = {'Total information': {
    'Version': python_vers,
    'Virtual environment name': pyenv_name,
    'Python executable location': python_ex_l,
    'Pip location': pip_l,
    'PYTHONPATH': python_path,
    'Installed packages': python_pack,
    'Site-package location': pack_loc}
}

with open("result.json", "w") as data:
    data.write(json.dumps(output, indent=4))
with open("result.yaml", "w") as data:
    yaml.dump(output, data, default_flow_style=False)
