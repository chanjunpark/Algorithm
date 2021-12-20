public class Member {
    private int verificationEmailStatus;
    public boolean isEmailVerified() {
        return verificationEmailStatus == 2;
    }
}
