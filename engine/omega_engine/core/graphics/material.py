class Material():
    def __init__(self, name, ns, ka, kd, ks, illum, ni = None, d = None):
        self.name = name
        self.ns = ns
        self.ka = ka
        self.kd = kd
        self.ks = ks
        self.ni = ni
        self.d = d
        self.illum = illum

    