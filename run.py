import subprocess
from subprocess import call
import sys

def install_requirements(requirements_file):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install" ,"-r", requirements_file])
        print('Thành công')
    except subprocess.CalledProcessError as e:
        print('lỗi!')

call(["python", "main.py"])

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    install_requirements(requirements_file)
