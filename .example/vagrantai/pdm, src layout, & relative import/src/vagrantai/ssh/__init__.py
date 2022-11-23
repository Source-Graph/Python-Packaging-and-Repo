from ssh import *

class SSH:
    def __init__(self, vagrant_instance):
        self.vagrant = vagrant_instance
        self.keyfile = self.vagrant.vagrant.keyfile()
        self.user_hostname = self.vagrant.vagrant.user_hostname()
        self.user_hostname_port = self.vagrant.vagrant.user_hostname_port()

    def test_ssh_string(self):
        return f"ssh -i {self.keyfile} {self.user_hostname}"

    def __str__(self):
        return self.test_ssh_string()

    def fabric_ssh(self):
        print(self.vagrant.name)
