from deco.utils import pressure_at, Depth

_gas_densities = {
    "h": 0.179,
    "n2": 1.251,
    "o2": 1.428,
}


class Gas:
    def __init__(self, perc_o2, perc_h=0):
        self._frac_o2 = perc_o2 / 100
        self._frac_h = perc_h / 100
        self._frac_n2 = 1 - self._frac_h - self._frac_o2

    def density_at(self, depth: Depth):
        pressure = pressure_at(depth)
        return round(
            self._frac_o2 * _gas_densities["o2"] * pressure
            + self._frac_h * _gas_densities["h"] * pressure
            + self._frac_n2 * _gas_densities["n2"] * pressure,
            2,
        )

    def ppo2_at(self, depth: Depth):
        return self._frac_o2 * pressure_at(depth)

    def pph_at(self, depth: Depth):
        return self._frac_h * pressure_at(depth)

    def ppn2_at(self, depth: Depth):
        return self._frac_n2 * pressure_at(depth)


AIR = Gas(perc_o2=21)

EAN_32 = Gas(perc_o2=32)

EAN_50 = Gas(perc_o2=50)
OXYGEN = Gas(perc_o2=100)

TX_21_35 = Gas(perc_o2=21, perc_h=35)
TX_18_45 = Gas(perc_o2=18, perc_h=45)
TX_15_55 = Gas(perc_o2=15, perc_h=55)
TX_12_65 = Gas(perc_o2=12, perc_h=65)
TX_10_70 = Gas(perc_o2=10, perc_h=70)
