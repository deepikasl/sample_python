import unittest
from app import App

class TestSuite(unittest.TestCase):
#test15
    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)

    def test2(self):
        app = App()
        app.calculate2()
        self.failIf(app.retrieve2() != 61)
        
    def test3(self):
        app = App()
        app.calculate3()
        self.failIf(app.retrieve3() != 48)

    def test4(self):
        app = App()
        app.calculate4()
        self.failIf(app.retrieve4() != 29)
        
    def test5(self):
        app = App()
        app.calculate5()
        self.failIf(app.retrieve5() != 70)

    def test6(self):
        app = App()
        app.calculate6()
        self.failIf(app.retrieve6() != 120)
        
    def test7(self):
        app = App()
        app.calculate7()
        self.failIf(app.retrieve7() != 88)

    def test8(self):
        app = App()
        app.calculate8()
        self.failIf(app.retrieve8() != 49)
        
    def test9(self):
        app = App()
        app.calculate9()
        self.failIf(app.retrieve9() != 222)

    def test10(self):
        app = App()
        app.calculate10()
        self.failIf(app.retrieve10() != 181)
        
    def test11(self):
        app = App()
        app.calculate11()
        self.failIf(app.retrieve11() != 128)

    def test12(self):
        app = App()
        app.calculate12()
        self.failIf(app.retrieve12() != 69)
      
    def test13(self):
        app = App()
        app.calculate13()
        self.failIf(app.retrieve13() != 302)

    def test14(self):
        app = App()
        app.calculate14()
        self.failIf(app.retrieve14() != 241)
        
    def test15(self):
        app = App()
        app.calculate15()
        self.failIf(app.retrieve15() != 168)
    
    def test16(self):
        app = App()
        app.calculate16()
        self.failIf(app.retrieve16() != 89)
        
    def test17(self):
        app = App()
        app.calculate17()
        self.failIf(app.retrieve17() != 292)

    def test18(self):
        app = App()
        app.calculate18()
        self.failIf(app.retrieve18() != 301)
        
    def test19(self):
        app = App()
        app.calculate19()
        self.failIf(app.retrieve19() != 108)

    def test20(self):
        app = App()
        app.calculate20()
        self.failIf(app.retrieve20() != 109)
        
    def test21(self):
        app = App()
        app.calculate21()
        self.failIf(app.retrieve21() != 462)

    def test22(self):
        app = App()
        app.calculate22()
        self.failIf(app.retrieve22() != 361)
      
    def test23(self):
        app = App()
        app.calculate23()
        self.failIf(app.retrieve23() != 248)

    def test24(self):
        app = App()
        app.calculate24()
        self.failIf(app.retrieve24() != 129)
        
    def test25(self):
        app = App()
        app.calculate25()
        self.failIf(app.retrieve25() != 542)
        
    def test26(self):
        app = App()
        app.calculate26()
        self.failIf(app.retrieve26() != 421)

    def test27(self):
        app = App()
        app.calculate27()
        self.failIf(app.retrieve27() != 288)
        
    def test28(self):
        app = App()
        app.calculate28()
        self.failIf(app.retrieve28() != 298)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
