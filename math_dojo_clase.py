class MathDojo:
    
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
        #    if type(nums[i]) is list or type(nums[i]) is tuple:
        #       for j in nums[i]:
        #           self.result += j
        #  else:
            self.result += nums[i]
        print("La suma es:")
        return self

    def subtract(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
            self.result -= nums[i]
        print("La resta es:")
        return self

    def avg(self, num, *nums):
        media = (self.add(num,*nums).result) /(len(nums)+1)
        print("El Promedio Obtenido es:")
        return media
        


        #self.result += num
        #for i in range(len(nums)):
        #    self.add(num, nums)/(len(nums)+1)
        # return self



# crear una instruccion:
md = MathDojo()
md1 = MathDojo()
md3 = MathDojo()

# para probar:
media = md3.avg(1,1)
print(media)

x = md.add(1, 1, 1,30).result
print(x)

y = md1.subtract(20, 5).result
print(y)
#y = md1.add(1, 1, 1).subtract(1, 2).add(1, 1).add(1, 1).result
# y2 = md.subtract(5, 1, 2, 9).result
# y3 = md.subtract(5, 1, 8, 4, 1, 1).result
# o1 = md.add(1, 1, 1).subtract(1, 1,).result

# print(o1)


# print(x1)
# print(x2)
# print(y)
# print(y2)
# print(y3)


# corre cada uno de los metodos algunos mas veces y valida el resultado!
