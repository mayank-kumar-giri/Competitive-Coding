import java.util.Scanner;

public class Question5 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int a;
        a = scanner.nextInt();
        if(a<0) {System.out.println("Number is negative");}
        if(a==0) {System.out.println("Number is neutral");}
        if(a>0) {System.out.println("Number is positive");}
    }
}