import unittest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)
    def test_add(self):
        self.assertEqual(30,20+10)

if _name=='main_':
    unittest.main()