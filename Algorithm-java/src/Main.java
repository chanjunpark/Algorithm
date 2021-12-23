public class Main {

    public static void main(String[] args) {

    }

    public AuthResult authenticate(String id, String pw) {
        Memeber mem = findOne(id);
        if(!mem.isEmailVerivied()){
            return AuthResult.NO_EMAIL_VERIFIED;
        }
    }
}
