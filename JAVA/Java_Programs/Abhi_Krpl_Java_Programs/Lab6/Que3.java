import java.util.Scanner;
import java.lang.Math;

public class Que3 {
    
    Que3() {
        System.out.print("Enter a number: ");
        Scanner s = new Scanner(System.in);
        int r1,r2;
        r1 = s.nextInt();
        System.out.print("Enter another number: ");
        r2 = s.nextInt();
        int r3=r1+r2;
        System.out.println("Addittion of 2 integers: "+r3);
    }
    
    Que3(float n1) {
        float n2;
        System.out.print("Enter a number: ");
        Scanner s = new Scanner(System.in);
        n2 = s.nextFloat();
        float n3=n1+n2;
        System.out.println("Addittion of 2 floats: "+n3);
    }
    
    Que3(double n1, double n2) {
        double n3=n1+n2;
        System.out.println("Addittion of 2 doubles: "+n3);
    }
    
    Que3(String n1, String n2) {
        Scanner s = new Scanner(System.in);
        String n3;
        n3 = n1+n2;
        System.out.println("Concatenation: "+n3);
    }
    
    public static void main(String args[]) {
        Que3 obj1 = new Que3();
        Que3 obj2 = new Que3(4);
        Que3 obj3 = new Que3(2,3);
        Que3 obj4 = new Que3("Abhishek ", "Kripal");
    }
}