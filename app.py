class App():
    def __init__(self):
        self.var1 = 15    
        self.var2 = 20
        self.var3 = 25
        self.var4 = 30
        self.var5 = 35
        self.var6 = 40    
        self.var7 = 45
        self.var8 = 50
        self.var9 = 55
        self.var10 = 60
        self.var11 = 65    
        self.var12 = 70
        self.var13 = 75
        self.var14 = 80
        self.var15 = 85

    def calculate(self):
        self.result = self.var1 * 4 + 2
    def calculate2(self):
        self.result2 = self.var2 * 3 + 1
    def calculate3(self):
        self.result3 = self.var3 * 2 - 2
    def calculate4(self):
        self.result4 = self.var4 * 1 - 1
    def calculate5(self):
        self.result5 = self.var5 * 4 / 2
    def calculate6(self):
        self.result6 = self.var6 * 3 / 1
    def calculate7(self):
        self.result7 = self.var7 * 2 - 2
    def calculate8(self):
        self.result8 = self.var8 * 1 - 1
    def calculate9(self):
        self.result9 = self.var9 * 4 + 2
    def calculate10(self):
        self.result10 = self.var10 * 3 + 1
    def calculate11(self):
        self.result11 = self.var11 * 2 - 2
    def calculate12(self):
        self.result12 = self.var12 * 1 - 1
    def calculate13(self):
        self.result13 = self.var13 * 4 + 2
    def calculate14(self):
        self.result14 = self.var14 * 3 + 1
    def calculate15(self):
        self.result15 = self.var15 * 2 - 2

    def retrieve(self):
        return self.result
    def retrieve2(self):
        return self.result2
    def retrieve3(self):
        return self.result3
    def retrieve4(self):
        return self.result4
    def retrieve5(self):
        return self.result5
    def retrieve6(self):
        return self.result6
    def retrieve7(self):
        return self.result7
    def retrieve8(self):
        return self.result8
    def retrieve9(self):
        return self.result9
    def retrieve10(self):
        return self.result10
    def retrieve11(self):
        return self.result11
    def retrieve12(self):
        return self.result12
    def retrieve13(self):
        return self.result13
    def retrieve14(self):
        return self.result14
    def retrieve15(self):
        return self.result15

if __name__ == "__main__":
    app = App()
    app.calculate()
    app.calculate2()
    app.calculate3()
    app.calculate4()
    app.calculate5()
    app.calculate6()
    app.calculate7()
    app.calculate8()
    app.calculate9()
    app.calculate10()
    app.calculate11()
    app.calculate12()
    app.calculate13()
    app.calculate14()
    app.calculate15()
    
    print(app.retrieve)
    print(app.retrieve2)
    print(app.retrieve3)
    print(app.retrieve4)
    print(app.retrieve5)
    print(app.retrieve6)
    print(app.retrieve7)
    print(app.retrieve8)
    print(app.retrieve9)
    print(app.retrieve10)
    print(app.retrieve11)
    print(app.retrieve12)
    print(app.retrieve13)
    print(app.retrieve14)
    print(app.retrieve15)
