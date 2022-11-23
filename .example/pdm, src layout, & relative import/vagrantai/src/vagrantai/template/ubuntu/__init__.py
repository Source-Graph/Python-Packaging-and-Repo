class UbuntuLTS:
    name = "UbuntuLTS"
    box = "generic/ubuntu2204"
    kvm = True

    @classmethod
    def __str__(cls):
        return f"{cls.name}, {cls.box}, kvm={cls.kvm}"
