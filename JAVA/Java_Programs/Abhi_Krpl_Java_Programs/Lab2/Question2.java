import java.util.Scanner;
import java.lang.Math;

public class Question2 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter 3 sides of triangle: ");
        int a,b,c;
        float s;
        double heron;
        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();
        s = (a+b+c)/2;
        heron = Math.sqrt(s*(s-a)*(s-b)*(s-c));
        System.out.println("Area of triangle using heron's formula: "+heron);
    }
}