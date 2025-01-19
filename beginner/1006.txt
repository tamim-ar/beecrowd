import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {

         Scanner sc = new Scanner(System.in);
         
         double A = sc.nextDouble()*2;
         double B = sc.nextDouble()*3;
         double C = sc.nextDouble()*5;
         double D = (A+B+C)/10;
         
         System.out.printf("MEDIA = %.1f\n", D);
    }
 
}