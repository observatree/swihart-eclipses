from math import sin, pi


ZEROTH_NEW_MOON = 2444226.6
LUNAR_SYNODIC_PERIOD = 29.5306
SJD_OFFSET = 2444000.0


def jd_new_moon(n):
    return ZEROTH_NEW_MOON + n * LUNAR_SYNODIC_PERIOD


# Swihart prefers to subtract 2444000.0 from JD
def sjd_from_jd(jd):
    return jd - SJD_OFFSET


def longitude_node(sjd):
    return 152.0 - 0.0529538 * (sjd - 238.5)


def longitude_sun(sjd):
    k = 0.985647 * (sjd - 238.5)
    return 279.0 + k + 2.0 * sin(k * pi / 180.0)


def longitude_difference(n):
    sjd = sjd_from_jd(jd_new_moon(n))
    return longitude_sun(sjd) - longitude_node(sjd)


def eclipses_of_1990():
    min_n = 125.5
    max_n = 136.5

    n = min_n

    while n <= max_n:
        print(n)
        n += 0.5


if __name__ == "__main__":
    eclipses_of_1990()
