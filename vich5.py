import math

class Result:
    
    def first_function(x: float, y: float):
        return math.sin(x)


    def second_function(x: float, y: float):
        return (x * y)/2


    def third_function(x: float, y: float):
        return y - (2 * x)/y


    def fourth_function(x: float, y: float):
        return x + y

    
    def default_function(x:float, y: float):
        return 0.0

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        else:
            return Result.default_function

    #
    # Complete the 'solveByEulerImproved' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    def solveByEulerImproved(f, e, a, y_a, b, h = 0.005):
        x = a 
        y = y_a 
        while x < b:
            basicXY = h * Result.get_function(f)(x, y)
            modifiedXY = h * Result.get_function(f)(x + h, y + basicXY)
            y = y + (basicXY + modifiedXY) / 2
            if abs(basicXY - modifiedXY) / 2 > e:
                h = h**2
            x = x + h
        return y
    

def tests():
    f1, e1, a1, y_a1, b1 = 1, 0.01, 0, 1, 1.5 #first function
    print("Test 1: ", Result.solveByEulerImproved(f1, e1, a1, y_a1, b1))
    f2, e2, a2, y_a2, b2 = 2, 0.001, 0, 1, 2 #second function
    print("Test 2: ", Result.solveByEulerImproved(f2, e2, a2, y_a2, b2))
    f3, e3, a3, y_a3, b3 = 3, 0.01, 0, 1, 1 #third function
    print("Test 3: ", Result.solveByEulerImproved(f3, e3, a3, y_a3, b3))
    f4, e4, a4, y_a4, b4 = 4, 0.01, 0, 1, 1 #fourth function
    print("Test 4: ", Result.solveByEulerImproved(f4, e4, a4, y_a4, b4))
    f5, e5, a5, y_a5, b5 = 1, 0.00001, 2, 0, 4 #low epsilon
    print("Test 5: ", Result.solveByEulerImproved(f5, e5, a5, y_a5, b5))


if __name__ == '__main__':
    tests()