import java.util.*;


class Solution {

    public ArrayList<String> compressString(String s, int unit) {
        ArrayList<String> unitString = new ArrayList<>();
        int start = 0;

        for(int idx = 0; idx < s.length(); idx++){
            if(idx != 0 && idx%unit == 0){
                unitString.add(s.substring(start,idx));
                start = idx;
            }
            if(idx/unit >= (s.length()-1)/unit){
                unitString.add(s.substring(idx,s.length()));
                break;
            }
        }

        return unitString;
    }



    public int solution(String s) {
        int answer = 0;
        int min = 1001;

        for(int unit=1; unit<=s.length(); unit++){
            ArrayList<String> tempList = new ArrayList<>();
            tempList = compressString(s,unit);
            String temp = "";
            int count = 1;
            for(int idx=1; idx<tempList.size(); idx++){
                if(tempList.get(idx-1).equals(tempList.get(idx))){
                    count++;
                }
                else{
                    if(count == 1){
                        temp += tempList.get(idx-1);
                    }
                    else{
                        temp += Integer.toString(count) + tempList.get(idx-1);
                    }
                    count = 1;
                }
            }
            if(count == 1){
                temp += tempList.get(tempList.size()-1);
            }
            else{
                temp += Integer.toString(count) + tempList.get(tempList.size()-1);
            }
            if(temp.length() < min){
                min = temp.length();
            }
        }

        answer = min;

        return answer;
    }
}
