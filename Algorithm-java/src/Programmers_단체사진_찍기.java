import java.util.*;


public class Programmers_단체사진_찍기 {

    class Solution {

        public static int count;

        public int solution(int n, String[] data) {
            int answer = 0;
            count = 0;

            ArrayList<String> members = new ArrayList<>(Arrays.asList("A", "C", "F", "J", "M", "N", "R", "T"));
            ArrayList<String> current = new ArrayList<>();

            getPermutation(current, members, data);

            answer = count;

            return answer;
        }

        public static void getPermutation(ArrayList<String> current, ArrayList<String> members, String[] constraints) {
            if(current.size() == members.size()){ // 만약 현재까지 멤버가 전체 멤버 수와 같아 졌다면(모두 자리를 잡았다면)
                if(violateConstraint(current, constraints)){ // 제약조건을 위반한 경우
                    current.remove(current.size()-1);
                }else{ // 제약조건을 준수한 경우
                    count ++;
                    current.remove(current.size()-1);
                }
            }
            else{
                for(int i=0; i < members.size(); i++){
                    String current_member = members.get(i);
                    if(current.contains(current_member) == false){ // 현재까지 멤버에 새로 추가하려는 멤버가 없을 때(중복 방지)
                        if(violateConstraint(current, constraints)){ // 만약 현재까지 멤버가 제약조건을 위배한다면? 정지!
                            break;
                        }
                        else { // 아니라면, 현재까지 멤버에 추가하려는 멤버를 넣고 한번 더 조합 뽑기.
                            current.add(current_member); // 현재까지 멤버에 새로운 멤버 추가
                            getPermutation(current, members, constraints); // 조합
                            current.remove(current_member); // 멤버 제거
                        }
                    }
                }
            }
        }

        public static int getDistance(ArrayList<String> current, String from, String to){
            int distance = current.indexOf(from) - current.indexOf(to);
            if(distance < 0){
                distance = -distance;
            }
            distance--;
            return distance;
        }

        public static boolean violateConstraint(ArrayList<String> current, String[] constraints){
            boolean isConstraint = false;
            for(int j=0; j < constraints.length; j++){
                if(isConstraint){
                    break;
                }
                if((current.contains(constraints[j].substring(0,1)))&&(current.contains(constraints[j].substring(2,3)))){
                    int distance = getDistance(current, constraints[j].substring(0,1), constraints[j].substring(2,3));
                    switch(constraints[j].substring(3,4)){
                        case "=":
                            if(distance != constraints[j].charAt(4)-'0'){
                                isConstraint = true;
                            }
                            break;
                        case "<":
                            if(distance >= constraints[j].charAt(4)-'0'){
                                isConstraint = true;
                            }
                            break;
                        case ">":
                            if(distance <= constraints[j].charAt(4)-'0'){
                                isConstraint = true;
                            }
                            break;
                        default:
                            break;
                    }
                }
            }
            return isConstraint;
        }

    }

/*

전체 경우의 수 : 8! (순열)
A~C=2 -> 어피치와 콘의 거리는 2이다.

1. 매번 배열을 만들 때마다 조건과 부합하는 지 검사 -> ㄱㄱ
2. 그냥 마구잡이로 만드는 방법 -> 시간초과 날듯;

*/
}
