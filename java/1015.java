import java.io.IOException;
import java.util.*;
import java.lang.Math;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
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