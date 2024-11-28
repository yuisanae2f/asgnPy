class IOBase:
    def Gets(self, prompt: str) -> str:
        """
        Get the string input from keyboard in showing windows.
        """
        raise NotImplementedError("No Imp")
    
    def Puts(self, prompt: str) -> None:
        """
        Put the string output to showing windows in any way.
        """
        raise NotImplementedError("No Imp")
    
    
    def TestDeposit(self):
        c1 = int(self.Gets("Give me a number to deposit"))
        c500 = c1 // 500
        c1 %= 500
        c100 = c1 // 100
        c1 %= 100
        c10 = c1 // 10
        c1 %= 10

        self.Puts(f"Output: {c500} {c100} {c10} {c1}")

    def TestDiff(self):
        n0 = int(self.Gets("Number first: "))
        n1 = int(self.Gets("Number second: "))

        ret = n1 - n0 if n1 > n0 else n0 - n1
        self.Puts(f"{ret}")