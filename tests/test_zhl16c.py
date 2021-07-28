import pytest
from hypothesis import given, settings
import hypothesis.strategies as st

from deco.gas import AIR
from deco.zhl16c import Compartment


@st.composite
def compartment(draw):
    return Compartment(
        n2_t_half=draw(st.integers(min_value=1, max_value=1000)),
        n2_a=draw(st.floats(min_value=0.1, max_value=1.5)),
        n2_b=draw(st.floats(min_value=0.1, max_value=1.5)),
        h_t_half=draw(st.integers(min_value=1, max_value=1000)),
        h_a=draw(st.floats(min_value=0.1, max_value=1.5)),
        h_b=draw(st.floats(min_value=0.1, max_value=1.5)),
    )


@given(
    p_gas=st.floats(min_value=0, max_value=1),
    t_half=st.integers(min_value=1, max_value=1000),
    n_halftimes=st.integers(min_value=1, max_value=5)
)
@settings(max_examples=1000)
def test_compartment_new_gas_loading(p_gas, t_half, n_halftimes):
    assert Compartment.new_gas_loading(
        p_begin=0, p_gas=p_gas, t_half=t_half, t=t_half*60 * n_halftimes
    ) == pytest.approx(p_gas - (0.5**n_halftimes)*p_gas)


@given(
    compartment=compartment(),
    n_halftimes=st.integers(min_value=1, max_value=3)
)
@settings(max_examples=100)
def test_compartment_tick(compartment, n_halftimes):
    gas = AIR
    depth = 20
    compartment.current_nitrogen_loading = 0
    p_gas = gas.ppn2_at(depth)
    for halftime in range(1, n_halftimes * 1):
        for second in range(compartment.n2_t_half * 60):
            compartment.tick(gas=gas, depth=depth)
        assert compartment.current_nitrogen_loading == pytest.approx(p_gas - (0.5**halftime)*p_gas)
