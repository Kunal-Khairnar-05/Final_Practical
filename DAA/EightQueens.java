import java.util.*;

public class EightQueens {

    public static List<List<String>> EQueenSol(int n, int firstCol){
        char[][] board = new char[n][n];
        List<List<String>> result = new ArrayList<>();

        for(int i=0; i<n; i++){
            for(int j=0;j<n;j++){
                board[i][j] = '.';
            }
        }

        board[0][firstCol] = 'Q';

        backtrack(1,board,result);
        return result;
    }

    public static void backtrack(int row, char[][] board, List<List<String>> result){
        if(row==board.length){
            result.add(construct(board));
            return;
        }


        for(int col = 0; col<board.length; col++){
            if(isSafe(board, row, col)){
                board[row][col] = 'Q';
                backtrack(row+1, board, result);
                board[row][col] = '.';
            }
        }
    }

    public static List<String> construct(char[][]board){
        List<String> res = new ArrayList<>();
        for(char[]ch : board){
            res.add(new String(ch));
        }
        return res;
    }

    public static boolean isSafe(char[][] board, int row, int col) {
        for(int i=0; i<row; i++){
            if(board[i][col]=='Q') return false;
        }

        for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j]=='Q') return false;
        }

        for(int i=row-1, j=col+1; i>=0 && j<board.length; i--, j++){
            if(board[i][j]=='Q') return false;
        }
        return true;
    }
    

    public static void main(String[] args) {
        List<List<String>> re = EQueenSol(8, 0);

        for(List<String> r : re){
            System.out.println(r);
        }
    }
}
