class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:


        # for row in matrix:
        #     print(row)

        # print()

        matrix.reverse()

        # for row in matrix:
        #     print(row)

        # print("")

        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for row in matrix:
        #     print(row)

        