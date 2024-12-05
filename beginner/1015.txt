import java.io.IOException;
import java.util.*;
import java.lang.Math;
 
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
        
        float X1 = sc.nextFloat();
        float Y1 = sc.nextFloat();
        float X2 = sc.nextFloat();
        float Y2 = sc.nextFloat();
        float X = X2-X1;
        float Y = Y2-Y1;
        float A = X*X+Y*Y;
        
        System.out.printf("%.4f\n",Math.sqrt(A));
    }
}