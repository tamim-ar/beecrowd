import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
         Scanner sc = new Scanner(System.in);
         int R = sc.nextInt();
         
         double pi = 3.14159;
        double volume = (4.0 / 3) * pi * Math.pow(R, 3);

        System.out.printf("VOLUME = %.3f\n", volume);
 
    }
 
}