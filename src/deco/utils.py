from datetime import timedelta

Duration = timedelta
Depth = float
Pressure = float


def pressure_at(depth: Depth) -> Pressure:
    return 1 + (depth / 10)


def depth_for(pressure: Pressure) -> Depth:
    return (pressure - 1) * 10
