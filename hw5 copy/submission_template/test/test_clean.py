import unittest
from pathlib import Path
import os, sys
from src.clean import clean_json
import json
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class CleanTest(unittest.TestCase):
    def setUp(self):
        dr=os.path.dirname(__file__)
        f1_path=os.path.join(dr,'fixtures','test_1.json')
        with open(f1_path) as f1:
            self.f1=f1.readline()
        f2_path=os.path.join(dr,'fixtures','test_2.json')
        with open(f2_path) as f2:
            self.f2=f2.readline()
        f3_path=os.path.join(dr,'fixtures','test_3.json')
        with open(f3_path) as f3:
            self.f3=f3.readline()
        f4_path=os.path.join(dr,'fixtures','test_4.json')
        with open(f4_path) as f4:
            self.f4=f4.readline()
        f5_path=os.path.join(dr,'fixtures','test_5.json')
        with open(f5_path) as f5:
            self.f5=f5.readline()
        f6_path=os.path.join(dr,'fixtures','test_6.json')
        with open(f6_path) as f6:
            self.f6=f6.readline()
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.

    def test_title(self):
        self.assertEqual(clean_json(self.f1,""),"")
        # Just an idea for a test; write your implementation
    def test_createAt(self):
        self.assertEqual(clean_json(self.f2,""),"")

    def test_valid_json(self):
        self.assertEqual(clean_json(self.f3,""),"")

    def test_valid_author(self):
        self.assertEqual(clean_json(self.f4,""),"")

    def test_count(self):
        a=json.loads(self.f5)
        try:
            numb= int(float(a["total_count"]))
            self.assertEqual(clean_json(self.f5,"")["total_count"],numb)
        except ValueError:
            self.assertEqual(clean_json(self.f5,""),"")

    def test_tags(self):
        a=json.loads(self.f6)
        n=len(a["tags"])
        for i in a["tags"]:
            for s in i:
                if s ==" ":
                    n+=1
        self.assertEqual(len(clean_json(self.f6,"")["tags"]),n)
if __name__ == '__main__':
    unittest.main()
