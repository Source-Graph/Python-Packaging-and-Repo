# works: import
# absolute: Works in IDE only if installed with '--editable install'!
from vagrantai.template import UbuntuLTS
from vagrantai.vagrantfile import Vagrantfile
# relative: works in '--editable install' but NOT IDE!
# from .template import UbuntuLTS
# from .vagrantfile import Vagrantfile


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
    test_vagrant()
