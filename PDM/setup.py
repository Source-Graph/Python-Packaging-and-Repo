#from: https://pdm.fming.dev/latest/#installation

linux = "curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -"
windows = "(Invoke-WebRequest -Uri https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py -UseBasicParsing).Content | python -"


pep582 = "pdm --pep582"

def configPep582():
    to_profile = subprocess.run(pep582)
    write_to_profile(to_profile)

def write_to_profile(block):
    pass
