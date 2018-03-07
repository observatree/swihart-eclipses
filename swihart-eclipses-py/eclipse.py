# THIS CODE IS FOR A CLASS
# IT IS NOT ADEQUATELY QA'D
# IT AGREES FOR SOME INTERESTING SPECIAL CASES
# DO NOT USE IT FOR ANYTHING IMPORTANT

from math import sin, pi, isclose


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
    return 278.0 + k + 2.0 * sin(k * pi / 180.0)


def longitude_difference(n):
    sjd = sjd_from_jd(jd_new_moon(n))
    return longitude_sun(sjd) - longitude_node(sjd)


def normalize_longitude(longitude):
    while longitude > 180.0:
        longitude -= 360.0
    return longitude


def classify_eclipse(n, normalized_longitude):
    normalized_longitude = abs(normalized_longitude)
    if isclose(n % 1, 0.0):
        # integer case, classifying solar eclipses
        if normalized_longitude <= 10.5:
            return "central eclipse of the Sun"
        elif normalized_longitude <= 16.4:
            return "partial eclipse of the Sun"
        else:
            return None
    else:
        # half-integer case, classifying lunar eclipses
        if normalized_longitude <= 5.0:
            return "total eclipse of the Moon"
        elif normalized_longitude <= 10.7:
            return "partial eclipse of the Moon"
        elif normalized_longitude <= 16.4:
            return "penumbral eclipse of the Moon"
        else:
            return None


def eclipses_of_n(min_n, max_n):

    n = min_n

    while n <= max_n:
        difference = longitude_difference(n)
        for normalized_longitude in [normalize_longitude(difference), normalize_longitude(difference + 180.0)]:
            classification = classify_eclipse(n, normalized_longitude)
            if classification:
                print("n =", n, "moon has normalized longitude difference", normalized_longitude, "and classification",
                      classification)
        n += 0.5


# 1990

def eclipses_of_1990():
    min_n = 124.5
    max_n = 136.0
    eclipses_of_n(min_n, max_n)


# 2017

# First moment of 2017
BEGIN_JD = 2457754.500000
BEGIN_SJD = 13754.5
BEGIN_N = 458.5

# Last moment of 2017
END_JD = 2458119.500000
END_SJD = 14119.5
END_N = 470.0


def eclipses_of_2017():
    eclipses_of_n(BEGIN_N, END_N)


# 2024

def eclipses_of_2024():
    eclipses_of_n(545.0, 557.0)


if __name__ == "__main__":
    eclipses_of_2017()


# Compare the 2017 output with the web:

# Feb 10–11, 2017 — Penumbral Lunar Eclipse.
# Feb 26, 2017 – Annular Solar Eclipse.
# Aug 7–8, 2017 — Partial Lunar Eclipse.
# Aug 21, 2017 – Total Solar Eclipse.

# The last one is n = 466.0, JD = 2457987.8596 and is the one I went to Oregon to see!
# Unfortunately our code predicts it as occurring at 1am PDT on August 22nd, but of course it occurred
# around 15 hours before that. Hmmm.

# Great animation "2017 Eclipse Shadow Cones":
# https://svs.gsfc.nasa.gov/4321
# also available here:
# https://www.youtube.com/watch?v=yKFPL9xBe_U

# Compare the 2024 output with the web:

# Mar 24–25, 2024 — Penumbral Lunar Eclipse.
# Apr 8, 2024 – Total Solar Eclipse.
# Sep 17–18, 2024 — Partial Lunar Eclipse.
# Oct 2, 2024 – Annular Solar Eclipse.

# Slight disagreement here. Our code says the partial lunar eclipse is penumbral.
