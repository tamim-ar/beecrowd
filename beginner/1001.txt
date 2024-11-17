import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);

        int A = myObj.nextInt();
        int B = myObj.nextInt();
        int X = A + B;

        System.out.println("X = " + X);
    }
}