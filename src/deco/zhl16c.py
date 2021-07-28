from deco.gas import Gas
from deco.utils import Depth, depth_for


class Compartment:
    def __init__(
        self,
        n2_t_half,
        n2_a,
        n2_b,
        h_t_half,
        h_a,
        h_b
    ):
        self.n2_t_half = n2_t_half
        self.n2_a = n2_a
        self.n2_b = n2_b
        self.h_t_half = h_t_half
        self.h_a = h_a
        self.h_b = h_b

        self.current_nitrogen_loading = 0.79
        self.current_helium_loading = 0

    def tick(self, depth: Depth, gas: Gas):
        self.current_helium_loading = self.new_gas_loading(
            self.current_helium_loading,
            gas.pph_at(depth),
            self.h_t_half,
            1
        )
        self.current_nitrogen_loading = self.new_gas_loading(
            self.current_nitrogen_loading,
            gas.ppn2_at(depth),
            self.n2_t_half,
            1
        )

    def ascent_ceiling(self, gradient_factor=1) -> Depth:
        p_comp = self.current_nitrogen_loading + self.current_helium_loading

        a = (self.n2_a * self.current_nitrogen_loading + self.h_a * self.current_helium_loading) / p_comp
        b = (self.n2_b * self.current_nitrogen_loading + self.h_b * self.current_helium_loading) / p_comp

        pressure_ceiling = (p_comp - a) * b
        gf_corrected_pressure_ceiling = p_comp + (pressure_ceiling - p_comp) * gradient_factor
        return depth_for(gf_corrected_pressure_ceiling)

    @staticmethod
    def new_gas_loading(p_begin, p_gas, t_half, t):
        return p_begin + (p_gas - p_begin) * (1 - 2 ** -((t / 60) / t_half))


class ZH_L16C:
    def __init__(self):
        # TODO: Verify the coefficients
        self._compartments = [
            Compartment(4,    1.2599, 0.5050, 1.51,   1.7424, 0.4245),
            Compartment(8,    1.0000, 0.6514, 3.02,   1.3830, 0.5747),
            Compartment(12.5, 0.8618, 0.7222, 4.72,   1.1919, 0.6527),
            Compartment(18.5, 0.7562, 0.7825, 6.99,   1.0458, 0.7223),
            Compartment(27,   0.6200, 0.8125, 10.21,  0.9220, 0.7582),
            Compartment(38.3, 0.5043, 0.8434, 14.48,  0.8205, 0.7957),
            Compartment(54.3, 0.4410, 0.8693, 20.53,  0.7305, 0.8279),
            Compartment(77,   0.4000, 0.8910, 29.11,  0.6502, 0.8553),
            Compartment(109,  0.3750, 0.9092, 41.2,   0.5950, 0.8757),
            Compartment(146,  0.3500, 0.9222, 55.19,  0.5545, 0.8903),
            Compartment(187,  0.3295, 0.9319, 70.69,  0.5333, 0.8997),
            Compartment(239,  0.3065, 0.9403, 90.34,  0.5189, 0.9073),
            Compartment(305,  0.2835, 0.9477, 115.29, 0.5181, 0.9122),
            Compartment(390,  0.2610, 0.9544, 147.42, 0.5176, 0.9171),
            Compartment(498,  0.2480, 0.9602, 188.24, 0.5172, 0.9217),
            Compartment(635,  0.2327, 0.9653, 240.3,  0.5119, 0.9267),
        ]

    def tick(self, depth: Depth, gas: Gas):
        for compartment in self._compartments:
            compartment.tick(depth, gas)

    def ascent_ceiling(self, gradient_factor=1):
        return max(compartment.ascent_ceiling(gradient_factor=gradient_factor) for compartment in self._compartments)
