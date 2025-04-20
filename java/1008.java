import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
         Scanner sc = new Scanner(System.in);
         
         int number = sc.nextInt();
         int hour = sc.nextInt();
         double salary = sc.nextDouble();
         
         System.out.println("NUMBER = "+number);
         System.out.printf("SALARY = U$ %.2f\n",hour*salary);
    }
 
}