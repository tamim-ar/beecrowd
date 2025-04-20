import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
         Scanner sc = new Scanner(System.in);
         
         String name = sc.next();
         double salary = sc.nextDouble();
         double sold = sc.nextDouble();
         
         System.out.printf("TOTAL = R$ %.2f\n",salary+sold*0.15);
    }
 
}