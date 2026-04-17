class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:


        # for row in matrix:
        #     print(row)

        # print()

        for i in range(len(matrix) // 2):
            matrix[i], matrix[-i-1] = matrix[-i-1], matrix[i]

        # for row in matrix:
        #     print(row)

        # print("")

        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                print(f"switching {matrix[i][j]} with {matrix[j][i]}")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for row in matrix:
        #     print(row)

        