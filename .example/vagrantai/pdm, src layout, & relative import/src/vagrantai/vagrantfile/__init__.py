import os
import platform
import subprocess
import vagrant

from vagrantai import template
from vagrantai import uni


class Vagrantfile:
    def __init__(self, name=template.UbuntuLTS.name, tmpl=template.UbuntuLTS):
        if name != tmpl.name:
            self.name = name
        else:
            self.name = tmpl.name
        self.box = tmpl.box
        self.path = f"{uni.Uni.instance_dir}/{self.name}"
        self.vagrantfile = f"{self.path}/Vagrantfile"

        uni.Uni.init()
        self.vagrant = vagrant.Vagrant(root=self.path)

    def make_dir(self):
        os.makedirs(self.path, exist_ok=True)

    def make_vagrantfile(self):
        self.make_dir()
        if not os.path.isfile(self.vagrantfile):
            self.vagrant.init(self.box)

    def open_dir(self):
        self.make_dir()

        if platform.system() == "Windows":
            os.startfile(self.path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", self.path])
        else:
            subprocess.Popen(["xdg-open", self.path])

    def up(self):
        if not self.is_running():
            if uni.Uni.has_kvm_libvirt():
                self.vagrant.up(provider="libvirt")
            else:
                self.vagrant.up()

    def halt(self):
        if self.is_running():
            self.vagrant.halt()

    def info(self):
        name = self.vagrant.status()[0][0]
        state = self.vagrant.status()[0][1]
        provider = self.vagrant.status()[0][2]
        print(f"name {name}, state {state}, provider {provider}")

    def is_running(self):
        return self.vagrant.status()[0][1] == "running"

    def get_ssh(self):
        self.vagrant.ssh()
        # Todo:

    def __str__(self):
        return f"{self.name}, {self.box}, {self.path}"

# https://github.com/pycontribs/python-vagrant
