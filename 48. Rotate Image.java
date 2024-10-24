class Solution {
    public void rotate(int[][] matrix) {
        // int (matrix.length) = matrix.length;
        for(int i=0; i<(matrix.length)-1; i++){            // Transpose of matrix - replace rows with columns
            for(int j=1+i; j<(matrix.length); j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // exchange rows
        int start = 0, end = (matrix.length)-1;
        for(int i=0; i<(matrix.length); i++){
            for(int j=0; j<((matrix.length)/2); j++){
                int temp = matrix[i][start+j];
                matrix[i][start+j] = matrix[i][end-j];
                matrix[i][end-j] = temp;
            }
            
        }
    }
}