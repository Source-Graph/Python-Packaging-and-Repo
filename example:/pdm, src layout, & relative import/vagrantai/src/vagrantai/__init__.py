# works:
# relative: works in IDE & '--editable install'
from .template import UbuntuLTS
from .vagrantfile import Vagrantfile

# absolute: Works in '--editable install' only
# from vagrantai.template import UbuntuLTS

def test_vagrant():
    name = "wordpress"
    vm1 = Vagrantfile(name)
    vm1.open_dir()

def test_template():
    print(UbuntuLTS.name)
    print(UbuntuLTS.box)
    print(UbuntuLTS.kvm)

if __name__ == '__main__':
    test_template()