public class Programmers_124_나라의_숫자 {
    class Solution {
        public String solution(int n) {
            String answer = convertBase(n);
            return answer;
        }

        public String convertBase(int n){
            String number = "";
            while(n >= 1){
                if(n%3 == 0){
                    number = Integer.toString(4) + number;
                    n = (n/3)-1;
                }
                else {
                    number = Integer.toString(n%3) + number;
                    n = n/3;
                }
            }

            return number;
        }
    }
}
