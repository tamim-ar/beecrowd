import java.io.IOException;
import java.util.*;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        /**
         * Escreva a sua solução aqui
         * Code your solution here
         * Escriba su solución aquí
         */
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