public class Programmers_멀쩡한_사각형 {
    import java.lang.Math;


    class Solution {
        public long solution(int w, int h) {
            long answer = 0;
            long remain = 0;
            long total = (long)w*(long)h;
            int gcd = getGCD(w, h);
            w = w/gcd;
            h = h/gcd;
            long partition = (long)w*(long)h;


            for(int x = 1; x <=w; x++){
                remain += getHeight((double)w,(double)h,(double)x);
            }
            long sub = partition - remain*2;
            answer = total - sub*gcd;
            return answer;
        }

        public static long getHeight(double w, double h, double x){
            long y = (long)(Math.floor(-(h/w)*x + h));
            return y;
        }

        public static int getGCD(int w, int h){
            while(h!=0){
                int r = w%h;
                w = h;
                h = r;
            }
            return w;
        }
    }
}
