class UbuntuDesktop:
    name = "UbuntuDesktop"
    box = "generic/ubuntu2204-desktop"
    kvm = True

    @classmethod
    def __str__(cls):
        return f"{cls.name}, {cls.box}, kvm={cls.kvm}"
