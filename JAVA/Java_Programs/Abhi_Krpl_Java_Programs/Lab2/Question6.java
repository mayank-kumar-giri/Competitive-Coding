import java.util.Scanner;

public class Question6 {
    public static void main(String args[]) {
        while(1>0)
        {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a 3 digit number: ");
        int a,c,b;
        a = scanner.nextInt();
        b = a;
        c = a%10;
        a = a/10;
        c = c + (a%10);
        a = a/10;
        c = c + a;
        if(b>=100&&b<=999)
        {System.out.println("Addittion of all digits is: "+c); break;}
        else
        {System.out.println("Not a 3 digit number");}
        }
    }
}