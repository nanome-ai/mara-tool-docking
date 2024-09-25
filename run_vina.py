import os

CURR_DIR = os.path.dirname(__file__)
VINA_PATH = os.path.join(CURR_DIR, "bins/vina")

def check_vina_version():
    command = f"{VINA_PATH} --version"
    output = os.popen(command).read()
    print(output)

if __name__ == "__main__":
    check_vina_version()