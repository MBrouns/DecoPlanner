import pytest

from deco.gas import AIR, EAN_32, Gas


def test_gas_density():
    assert AIR.density_at(0) == pytest.approx(1.29)
    assert EAN_32.density_at(34) == pytest.approx(5.75)
    assert EAN_32.density_at(40) == pytest.approx(6.54)
    assert Gas(12, 35).density_at(50) == pytest.approx(5.38)
    assert Gas(18, 35).density_at(61) == pytest.approx(6.44)

def test_pn2():
    assert AIR.ppn2_at(0) == 0.79
    assert AIR.ppn2_at(30) == 3.16
