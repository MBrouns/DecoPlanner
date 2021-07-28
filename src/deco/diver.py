from datetime import timedelta

from deco.gas import Gas
from deco.utils import Depth, Duration
from deco.zhl16c import ZH_L16C

DEPTH_CHANGE_RATE = 9  # meter / second


class Diver:
    def __init__(self, deco_model=None):
        ...
        self._depth: Depth = 0
        self._time: int = 0
        self._deco_model = deco_model or ZH_L16C()

    def stay(self, duration: Duration) -> 'Diver':
        """
        Stay at the current depth for `duration`

        :param duration: the duration for which to stay at the current depth
        :return:
        """
        ...

    def change_depth_to(self, depth: Depth, during: Duration = None) -> 'Diver':
        """
        Change the depth to `depth`

        :param depth:
        :param during: the time the depth change takes
        :return:
        """
        ...

    def switch_gas(self, gas: Gas):

        ...
