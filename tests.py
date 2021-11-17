import unittest
from pizza import factorial, choose
from sum_numbers import sum_to
from seconds import to_seconds
from selection_sort import index_of_min, selection_sort
from palindrome_3 import is_palindrome

class Tests(unittest.TestCase):
  def test_sum_to(self):
    self.assertEqual(sum_to(0), 0)
    self.assertEqual(sum_to(1), 1)
    self.assertEqual(sum_to(5), 15)
    self.assertEqual(sum_to(10), 55)
    self.assertEqual(sum_to(15), 120)
    self.assertEqual(sum_to(35), 630)
    self.assertEqual(sum_to(50), 1275)

  def test_factorial(self):
    self.assertEqual(factorial(3),6)
    self.assertEqual(factorial(4),24)
    self.assertEqual(factorial(0),1)
    self.assertEqual(factorial(1),1)
    self.assertEqual(factorial(6),720)
    self.assertEqual(factorial(14),87178291200)
    self.assertEqual(factorial(20),2432902008176640000)

  def test_combinations(self):
    self.assertEqual(choose(19,11),75582)
    self.assertEqual(choose(16,10),8008)
    self.assertEqual(choose(8,4),70)
    self.assertEqual(choose(13,7),1716)
    self.assertEqual(choose(30,20),30045015)

  def test_seconds(self):
    self.assertEqual(to_seconds(2, 30, 10),9010)
    self.assertEqual(to_seconds(2, 0, 0), 7200)
    self.assertEqual(to_seconds(0, 2, 0), 120)
    self.assertEqual(to_seconds(0, 0, 42), 42)
    self.assertEqual(to_seconds(0, -10, 10), -590)

  def test_index_of_min(self):
    self.assertEqual(index_of_min([1,2,3],0),0)
    self.assertEqual(index_of_min([11,9,3,5,10],0),2)
    self.assertEqual(index_of_min([11,9,3,5,10],1),2)
    self.assertEqual(index_of_min([11,9,3,5,10],3),3)
    self.assertEqual(index_of_min([15],0),0)
    self.assertEqual(index_of_min([15, 3, 0, 2, 11, 9, 4, 7, 7, 8, 11, 9, 5, 1, 0, 18, 10, 19, 13],4),14)
    self.assertEqual(index_of_min([9, 16, 2, 10],0),2)
    self.assertEqual(index_of_min([13, 5, 1, 16, 5, 10, 13, 8, 3, 7, 17, 3, 13, 1, 4, 10, 18, 18, 4, 17, 12, 15, 0, 13, 1, 16],15),22)
    self.assertEqual(index_of_min([10, 7, 19, 16, 5, 10, 5, 1, 5, 4, 6, 2, 3, 7, 12, 8, 9, 18, 1, 10, 7, 18],6),7)
    self.assertEqual(index_of_min([18, 8],0),1)
    self.assertEqual(index_of_min([9, 14, 3, 15, 3, 1, 10, 16, 15, 12, 2, 6, 19],5),5)
    self.assertEqual(index_of_min([17, 0, 6, 17, 2, 12, 13, 12, 1, 0, 5, 5, 5],7),9)
    self.assertEqual(index_of_min([11, 10, 4, 5, 11, 6, 2, 0, 19, 3, 3, 19, 4, 17, 8, 0, 12, 17],7),7)
    self.assertEqual(index_of_min([1, 6, 18, 13, 4, 4, 1, 7, 6, 18, 2, 13, 12, 19, 8, 12, 17, 17, 8, 1, 19, 15, 2, 5, 16, 6, 10],21),22)
    self.assertEqual(index_of_min([13, 19, 9, 10, 17, 14, 5, 18, 7, 1, 13, 13, 12, 10, 10, 5, 5, 0, 9, 1, 9, 0, 4, 7, 17, 14],19),21)
    self.assertEqual(index_of_min([6, 2, 6, 6, 15, 18, 2, 17, 17, 8, 1, 6, 1, 3, 4, 15, 5, 18, 3, 3, 5, 11, 0],13),22)
    self.assertEqual(index_of_min([12, 19, 14, 19, 11, 19, 1, 7, 16, 13, 13, 0, 11, 15, 1, 0, 19, 6],15),15)
    self.assertEqual(index_of_min([15, 13, 3, 13, 12, 16, 13, 19, 8, 1, 2, 3, 4, 6, 18, 7, 6, 17],9),9)

  def test_selection_sort(self):
    l = [16, 5, 10, 17, 18, 9]
    selection_sort(l)
    self.assertEqual(l, [5, 9, 10, 16, 17, 18])
    l = [18, 13, 4, 11, 1, 3, 11, 12, 15, 16, 4, 4, 17, 18, 14, 16, 2, 14, 4, 6, 14, 10, 2, 5, 5, 19]
    selection_sort(l)
    self.assertEqual(l,
        [1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 10, 11, 11, 12, 13, 14, 14, 14, 15, 16, 16, 17, 18, 18, 19])
    l = [7, 9, 19, 4, 6, 7]
    selection_sort(l)
    self.assertEqual(l, [4, 6, 7, 7, 9, 19])
    l = [4, 16, 3, 16, 7, 3, 11, 1, 14, 15, 14, 2, 11, 16, 10, 19]
    selection_sort(l)
    self.assertEqual(l, [1, 2, 3, 3, 4, 7, 10, 11, 11, 14, 14, 15, 16, 16, 16, 19])
    l =  [7, 16, 3, 17, 11, 6, 13, 18, 2, 14, 6, 18, 7, 8, 3, 18, 14, 1, 17, 13, 2, 16, 9, 10, 9, 2, 13, 9]
    selection_sort(l)
    self.assertEqual(l,
                      [1, 2, 2, 2, 3, 3, 6, 6, 7, 7, 8, 9, 9, 9, 10, 11, 13, 13, 13, 14, 14, 16, 16, 17, 17, 18, 18,
                       18])
    l =  [10, 11, 6, 1, 14, 10, 0]
    selection_sort(l)
    self.assertEqual(l, [0, 1, 6, 10, 10, 11, 14])
    l =  [15, 16, 16, 3, 3, 17, 4, 7, 6, 15]
    selection_sort(l)
    self.assertEqual(l, [3, 3, 4, 6, 7, 15, 15, 16, 16, 17])
    l =  [5, 10, 9, 10, 1, 3, 5, 9, 12, 9, 3, 18, 14, 9, 5, 7, 15, 5, 17, 4, 11, 4, 5, 9, 10, 11, 16, 9]
    selection_sort(l)
    self.assertEqual(l,
        [1, 3, 3, 4, 4, 5, 5, 5, 5, 5, 7, 9, 9, 9, 9, 9, 9, 10, 10, 10, 11, 11, 12, 14, 15, 16, 17, 18])
    l =  [5, 16, 17, 13, 4, 8, 8, 9, 11]
    selection_sort(l)
    self.assertEqual(l, [4, 5, 8, 8, 9, 11, 13, 16, 17])
    l =  [6, 11, 3, 5, 0]
    selection_sort(l)
    self.assertEqual(l, [0, 3, 5, 6, 11])


  def test_palindrome_3(self):
      self.assertTrue(is_palindrome("racecar"))
      self.assertTrue(is_palindrome("kayak"))
      self.assertFalse(is_palindrome("otton"))
      self.assertTrue(is_palindrome("otto"))
      self.assertTrue(is_palindrome("wontloversrevoltnow"))
      self.assertTrue(is_palindrome("nanananananan"))
      self.assertFalse(is_palindrome("noen"))

if __name__ == '__main__':
    unittest.main()
