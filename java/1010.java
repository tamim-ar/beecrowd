import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
         Scanner sc = new Scanner(System.in);
         
         int code1 = sc.nextInt();
         int unit1 = sc.nextInt();
         double price1 = sc.nextDouble();
         
        int code2 = sc.nextInt();
        int unit2 = sc.nextInt();
        double price2 = sc.nextDouble();
        
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", unit1*price1+unit2*price2);
    }
 
}