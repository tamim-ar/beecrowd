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
         double A = sc.nextDouble();
         double B = sc.nextDouble();
         double C = sc.nextDouble();
         
         double pi = 3.14159;
         
         double f1 = (A * C) / 2.0;
         double f2 = pi * Math.pow(C, 2);
         double f3 = ((A + B) / 2.0) * C;
         double f4 = Math.pow(B, 2);
         double f5 = A * B;
         
         System.out.printf("TRIANGULO: %.3f\n",f1);
         System.out.printf("CIRCULO: %.3f\n",f2);
         System.out.printf("TRAPEZIO: %.3f\n",f3);
         System.out.printf("QUADRADO: %.3f\n",f4);
         System.out.printf("RETANGULO: %.3f\n",f5);
         
 
    }
 
}