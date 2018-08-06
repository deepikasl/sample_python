import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        app.calculate2()
        self.failIf(app.retrieve() != 62)
        self.failIf(app.retrieve2() != 82)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
