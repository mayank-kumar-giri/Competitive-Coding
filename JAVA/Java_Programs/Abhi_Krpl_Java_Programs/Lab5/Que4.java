import java.util.Scanner;
import static java.lang.Math.pow;


class Compound {
    static double func(int p, int r, int period)
    {
        double compound;
        compound = p*(Math.pow(1+r,period)-1);
        return compound;
    }
}

public class Que4 {
    public static void main(String args[]) {
        int principal,rate,period;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter principal/original amount: ");
        principal = scanner.nextInt();
        System.out.print("Enter rate per period: ");
        rate = scanner.nextInt();
        System.out.print("Enter number of period: ");
        period = scanner.nextInt();
        
        System.out.println("Compound Interest: "+Compound.func(principal,rate,period));
        
    }
}