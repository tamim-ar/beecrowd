import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        double n = 3.14159;
        double R = myObj.nextDouble();

        double A = n * (R * R);

        System.out.printf("A=%.4f\n", A);
    }
}
