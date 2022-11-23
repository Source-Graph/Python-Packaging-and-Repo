import os, pathlib


class Uni:
    vagrant_home = f"{pathlib.Path.home()}/.uni/hyperion/vagrant"
    instance_dir = f"{vagrant_home}/instance"

    def __init__(self):
        Uni.init()

    @classmethod
    def init(cls):
        os.makedirs(cls.instance_dir, exist_ok=True)

    @classmethod
    def __str__(cls):
        return f"{cls.vagrant_home}, {cls.instance_dir}"

    @staticmethod
    def has_kvm_libvirt():
        return False