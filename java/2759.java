import java.io.IOException;
import java.util.*;

public class Main {
 
    public static void main(String[] args) throws IOException {

         Scanner sc = new Scanner(System.in);
         
         String A = sc.next();
         String B = sc.next();
         String C = sc.next();
         
         System.out.println("A = "+A+", B = "+B+", C = "+C);
         System.out.println("A = "+B+", B = "+C+", C = "+A);
         System.out.println("A = "+C+", B = "+A+", C = "+B);
    }
 
}