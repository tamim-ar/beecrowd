import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner sc = new Scanner(System.in);
        
        int X = sc.nextInt();
        float Y = sc.nextFloat();
        
        System.out.printf("%.3f km/l\n",X/Y);
        
 
    }
 
}