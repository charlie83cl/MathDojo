class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *x):
        for obj in x:
            if type(obj) == list:
                for value in obj:
                    self.result += value
            elif type(obj) == int:
                self.result += obj
        # isinstance <-- python
        return self

list1 = [1,2,3,4,6]
list2 = [3,5,7,9]

md = MathDojo().add(list2,list1,5,6,list2).subtract(10,list1).result
#md = MathDojo().add(1,1,1,1,1,1,1,1).result

print(md)