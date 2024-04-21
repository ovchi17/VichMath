import math
import os
import random
import re
import sys

class Result:
    error_message = ""
    has_discontinuity = False
    
    def first_function(x: float):
        return 1 / x


    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps)/Result.eps + math.sin(-Result.eps)/-Result.eps)/2 
        return math.sin(x)/x


    def third_function(x: float):
        return x*x+2


    def fourth_function(x: float):
        return 2*x+2


    def five_function(x: float):
        return math.log(x)

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
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #

    def showError(text):
        Result.error_message = text
        Result.has_discontinuity = True

    
    def calculate_integral(a, b, f, epsilon, n = 5, step = 5):
        workFunction = Result.get_function(f)
        isNegative = 1
        if a > b:
            change = a
            a = b
            b = change
            isNegative = -1
        previousIntegral = 0
        currentIntegral = 0
        while True:
            currentIntegral = 0
            stepValue = (b - a) / n
            for i in range(n):
                xMiddle = (i + 0.5) * stepValue + a
                try:
                    functionResult = workFunction(xMiddle)
                except:
                    Result.showError("Integrated function has discontinuity or does not defined in current interval")
                    return 0
                currentIntegral = currentIntegral + functionResult * stepValue
            if abs(currentIntegral - previousIntegral) <= epsilon:
                return currentIntegral * isNegative
            previousIntegral = currentIntegral
            n = n + step


    def startExamples():
        a1, b1, f1 = 1, 2, 1
        epsilon1 = 0.01
        result1 = Result.calculate_integral(a1, b1, f1, epsilon1)
        if not Result.has_discontinuity:
            print(str(result1) + '\n')
        else:
            print(Result.error_message + '\n')
            Result.has_discontinuity = False

        a2 = 0
        b2 = 2
        f2 = 3
        epsilon2 = 0.01
        result2 = Result.calculate_integral(a2, b2, f2, epsilon2)
        if not Result.has_discontinuity:
            print(str(result2) + '\n')
        else:
            print(Result.error_message + '\n')
            Result.has_discontinuity = False

        a3 = -1
        b3 = 1
        f3 = 1
        epsilon3 = 0.01
        result3 = Result.calculate_integral(a3, b3, f3, epsilon3)
        if not Result.has_discontinuity:
            print(str(result3) + '\n')
        else:
            print(Result.error_message + '\n')
            Result.has_discontinuity = False

        a4 = 1
        b4 = 6
        f4 = 4
        epsilon4 = 0.01
        result4 = Result.calculate_integral(a4, b4, f4, epsilon4)
        if not Result.has_discontinuity:
            print(str(result4) + '\n')
        else:
            print(Result.error_message + '\n')
            Result.has_discontinuity = False

        a5 = 1
        b5 = 2
        f5 = 5
        epsilon5 = 0.01
        result5 = Result.calculate_integral(a5, b5, f5, epsilon5)
        if not Result.has_discontinuity:
            print(str(result5) + '\n')
        else:
            print(Result.error_message + '\n')
            Result.has_discontinuity = False
        





if __name__ == '__main__':
    Result.startExamples()
        
    print()