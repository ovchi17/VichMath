class Solution:
    isSolutionExists = True
    errorMessage = ""

    def solveByGauss(n, matrix):
        a = []
        b = []
        aSave = []
        bSave = []
        fl = 0
        for x in range(n):
            ms = []
            for y in range(n):
                ms.append(matrix[x][y])
            a.append(ms)
            aSave.append(ms)
            b.append(matrix[x][len(matrix[x]) - 1])
            bSave.append(matrix[x][len(matrix[x]) - 1])
        for i in range(n):
            mxNum = abs(a[i][i])
            mxSt = i
            for j in range(i + 1, n):
                if abs(a[j][i]) > mxNum:
                    mxSt = j
                    mxNum = abs(a[j][i])
            bChange = b[mxSt]
            b[mxSt] = b[i]
            b[i] = bChange
            aChange = a[mxSt]
            a[mxSt] = a[i]
            a[i] = aChange

            if a[i][i] == 0:
                Solution.isSolutionExists = False
                Solution.errorMessage = "The system has no roots of equations or has an infinite set of them."
                fl = 1
            else:
                workNum = a[i][i]
                change = []
                for j in a[i]:
                    change.append(j / workNum)
                a[i] = change
                b[i] = b[i] / workNum
                for j in range(n):
                    if i != j:
                        workNum = a[j][i]
                        change = []
                        for x in range(n):
                            change.append(a[j][x] - workNum * a[i][x])
                        a[j] = change
                        b[j] = b[j] - workNum * b[i]
        if fl == 0:
            ans = []
            resultX = [0] * n
            for i in range(n - 1, -1, -1):
                resultX[i] = b[i]
                for j in range(i + 1, n):
                    b[i] -= resultX[j] * a[i][j]
            for i in range(n):
                resultX[i] = round(resultX[i], 3) 
                ans.append(resultX[i])

            devia = []
            for i in range(n):
                devia.append(bSave[i])
                for j in range(n):
                    devia[i] = devia[i] - aSave[i][j] * resultX[j]
                    devia[i] = round(devia[i], 3)
                ans.append(devia[i])
            return ans
        else:
            return []
            

    def test():
        n1 = 3
        matrix1 = [[4, 2, -1, 1], [5, 3, -2, 2], [3, 2, -3, 0]]
        if (Solution.solveByGauss(n1, matrix1) == [-1, 3, 1, 0, 0, 0]):
            print("test1 passed")
        else:
            print("test1 failed")
        n2 = 3
        matrix2 = [[0, 1, 2, 3], [1, 2, 3, 4], [4, 5, 6, 7]]
        if (Solution.solveByGauss(n2, matrix2) == []):
            print("test2 passed")
        else:
            print("test2 failed")
        n3 = 3
        matrix3= [[2.74, -1.18, 3.17, 2.18], [1.12, 0.83, -2.16, -1.15], [0.18, 1.27, 0.76, 3.23]]
        if (Solution.solveByGauss(n3, matrix3) == [0.097, 1.773, 1.264, -0.001, -0.001, 0]):
            print("test3 passed")
        else:
            print("test3 failed")
        n4 = 3
        matrix4 = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 11]]
        if (Solution.solveByGauss(n4, matrix4) == []):
            print("test4 passed")
        else:
            print("test4 failed")
        n5 = 4
        matrix5 = [[2, 5, 4, 1, 20], [1, 3, 2, 1, 11], [2, 10, 9, 7, 40], [3, 8, 9, 2, 37]]
        if (Solution.solveByGauss(n5, matrix5) == [1, 2, 2, 0, 0, 0, 0, 0]):
            print("test5 passed")
        else:
            print("test5 failed")
            



if __name__ == '__main__':
    Solution.test()
