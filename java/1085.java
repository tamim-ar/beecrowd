import java.io.IOException;
import java.util.*;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        int i;
        long sum = 0;

        for (i = A; i <= B; i++){
            sum = sum + i;
        }

        System.out.println(sum);
 
    }
 
}