import unittest
from MyNotebook import hoge, fuga
# import AnotherNotebook as anothernotebook
import os
import time

class MyNotebookTests(unittest.TestCase):
  
  def test_hoge(self):
    self.assertEqual(hoge(3), 'hogehogehoge')
    self.assertNotEqual(hoge(2), 'hoge')

  def test_fuga(self):
    self.assertEqual(fuga(3), 'fugafugafuga')
    self.assertNotEqual(fuga(2), 'fuga')

  def test_anothernotebook(self):
    os.system("python3 AnotherNotebook.py 1 2")
    with open("myOutFile.txt") as f:
      content = f.readlines()
    # Check
    self.assertEqual(content, ['1 2'])
    self.assertNotEqual(content, ['2 2'])

suite = unittest.TestLoader().loadTestsFromTestCase(MyNotebookTests)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(MyNotebookTests)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)