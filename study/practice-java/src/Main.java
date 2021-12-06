public class Main {
    public static void main(String[] args){
        System.out.println("hello world");

        int a = 3;
        int b = 5;
        char c = 'c';
        String str = new String("hello");

        for(int i=0 ; i<10;i++){
            System.out.println(i);
        }
        System.out.println(addNum(a));
        System.out.println(str);
    }

    private static int addNum(int number) {
        int answer = number + 100;
        return answer;
    }
}
