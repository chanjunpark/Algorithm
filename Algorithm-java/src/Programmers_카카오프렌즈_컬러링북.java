import java.util.*;


public class Programmers_카카오프렌즈_컬러링북 {


    class Solution {

        public static int[] answer;
        public static boolean [][] is_visited;
        public static int count;
        public static int m;
        public static int n;

        public int[] solution(int m, int n, int[][] picture) {

            is_visited = new boolean[m][n];
            this.m = m;
            this.n = n;
            count = 0;
            int numberOfArea = 0;
            int maxSizeOfOneArea = -1;

            for(int row=0; row<m; row++){
                for(int col=0; col<n; col++){
                    if((picture[row][col] != 0) && (is_visited[row][col] == false)){
                        numberOfArea ++;
                        searchSpace(row, col, picture[row][col], picture);
                        if(count > maxSizeOfOneArea){
                            maxSizeOfOneArea = count;
                        }
                        count = 0;
                    }
                }
            }

            answer = new int[2];
            answer[0] = numberOfArea;
            answer[1] = maxSizeOfOneArea;
            return answer;
        }

        public static boolean searchSpace(int row, int col, int color, int[][] picture){
            if((row < 0 || row >= m)||(col < 0 || col >= n)||(picture[row][col] != color)||(is_visited[row][col] == true)){
                return false;
            } else{
                is_visited[row][col] = true;
                count++;
                searchSpace(row+1, col, color, picture);
                searchSpace(row-1, col, color, picture);
                searchSpace(row, col+1, color, picture);
                searchSpace(row, col-1, color, picture);
            }
            return false;
        }
    }
}
