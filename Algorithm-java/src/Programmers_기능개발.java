import java.util.*;
import java.lang.Math;


public class Programmers_기능개발 {


    class Solution {
        public int[] solution(int[] progresses, int[] speeds) {

            int[] answer = new int[101];
            int header = 0;
            int current = 0;
            int pointer = 0;
            while(pointer < progresses.length){
                int times = (int) Math.ceil((100.0 - (double)progresses[pointer])/(double)speeds[pointer]);
                for(int idx = pointer; idx < progresses.length; idx++){
                    if(progresses[idx]+(speeds[idx]*times) >= 100){
                        pointer ++;
                    } else{
                        break;
                    }
                }
                answer[header++] = pointer - current;
                current = pointer;
            }

            answer = Arrays.copyOfRange(answer, 0, header);

            return answer;
        }
    }

}
