import java.io.IOException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        double A = sc.nextDouble();
        double B = sc.nextDouble();

        double C = ((A * 3.5) + (B * 7.5)) / 11;

        System.out.printf("MEDIA = %.5f\n", C);

    }

}