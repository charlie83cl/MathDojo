    def test02(self):
        md = MathDojo()
        self.assertEqual(md.add(1, 1, 1, 1).result, 4)
    
    def test03(self):
        md = MathDojo()
        self.assertEqual(md.subtract(100, 50, 10, 10).result, -170)

    def test04(self):
        md = MathDojo()
        self.assertEqual(md.subtract(-100, 1).result, 99)

