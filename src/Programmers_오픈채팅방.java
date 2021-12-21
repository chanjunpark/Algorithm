import java.util.ArrayList;
import java.util.HashMap;

public class Programmers_오픈채팅방 {


    class Member {
        private final String uid;
        private String name;

        public Member(String uid, String name){
            this.uid = uid;
            this.name = name;
        }
        public void setName(String name){
            this.name = name;
        }

        public String getName(){
            return name;
        }

        public String getUID(){
            return uid;
        }

    }

    class Solution {
        public String[] solution(String[] record) {
            ArrayList<Member> nameList = new ArrayList<>();
            ArrayList<String> actionList = new ArrayList<>();
            HashMap<String, Member> userList = new HashMap<>();
            ArrayList<String> result = new ArrayList<>();

            for(int i = 0; i < record.length; i++){
                String[] info = record[i].split(" ");
                if(info[0].equals("Change")){
                    Member user = userList.get(info[1]);
                    user.setName(info[2]);

                } else if(info[0].equals("Leave")){
                    Member user = userList.get(info[1]);
                    nameList.add(user);
                    actionList.add("님이 나갔습니다.");

                } else {
                    boolean flag = false;
                    if(userList.containsKey(info[1])){
                        Member user = userList.get(info[1]);
                        user.setName(info[2]);
                        nameList.add(user);
                        actionList.add("님이 들어왔습니다.");
                    } else{
                        Member user = new Member(info[1], info[2]);
                        userList.put(info[1], user);
                        nameList.add(user);
                        actionList.add("님이 들어왔습니다.");
                    }
                }
            }

            for(int i = 0; i < nameList.size(); i++){
                String name = nameList.get(i).getName();
                String action = actionList.get(i);
                result.add(name + action);
            }

            String[] answer = result.stream().toArray(String[]::new);

            return answer;
        }
    }
}
