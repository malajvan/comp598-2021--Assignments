import unittest
from pathlib import Path
import os, sys,json
from src.compile_word_counts import do_word_count
from src.compute_pony_lang import do_pony_lis

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class TasksTest(unittest.TestCase):
    def setUp(self):
        dir = os.path.dirname(__file__)
        self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
        self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
        self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')
        print("\nRUNNING TEST_TASK")


    def test_task1(self):
        # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print("RUNNING TEST FOR TASK 1")
        with open(self.true_word_counts,'r') as f:
            self.assertEqual(do_word_count(self.mock_dialog),json.load(f))
        print("OK")

    def test_task2(self):
        # use self.true_word_counts self.true_tf_idfs; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
        print("RUNNING TEST FOR TASK 2")
        with open(self.true_tf_idfs,'r') as f:
            self.assertEqual(do_pony_lis(self.true_word_counts,3),json.loads(f.read()))
        print("OK")

if __name__ == '__main__':
    unittest.main()
