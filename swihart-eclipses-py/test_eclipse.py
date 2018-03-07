import unittest

from eclipse import jd_new_moon, sjd_from_jd


class MyTestCase(unittest.TestCase):
    def test_third_new_moon(self):
        result = jd_new_moon(3)
        self.assertAlmostEqual(2444315.1918, result, 7)  # to 7 decimal places

    def test_sjd_from_jd(self):
        result = sjd_from_jd(2444000.1234)
        self.assertAlmostEqual(0.1234, result, 7)  # to 7 decimal places


if __name__ == '__main__':
    unittest.main()
