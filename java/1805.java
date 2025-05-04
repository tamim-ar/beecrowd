import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();
        
        // Using arithmetic progression formula: Sum = n(a1 + an)/2
        // where n is the number of terms, a1 is first term, an is last term
        long n = B - A + 1;
        long sum = (n * (A + B)) / 2;
        
        System.out.println(sum);
        sc.close();
    }
}
