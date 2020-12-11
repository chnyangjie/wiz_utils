from unittest import TestCase

from wiz_utils.array_utils import ArrayUtils


class TestArrayUtils(TestCase):
    def test_is_empty(self):
        self.assertTrue(ArrayUtils.is_empty(None))
        self.assertTrue(ArrayUtils.is_empty([]))
        self.assertFalse(ArrayUtils.is_empty([None, ]))
        self.assertFalse(ArrayUtils.is_empty([1, ]))

    def test_spilt(self):
        ArrayUtils.spilt([], 0)
