import pytest

from deco.utils import pressure_at, depth_for


def test_pressure_at():
    assert pressure_at(0) == pytest.approx(1)
    assert pressure_at(10) == pytest.approx(2)


def test_depth_for():
    assert depth_for(1) == 0
    assert depth_for(2) == 10
