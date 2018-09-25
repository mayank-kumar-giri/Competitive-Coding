import java.util.Scanner;
import java.lang.Math;

public class Que2 {
    
    Que2() {
        System.out.print("Enter the radius of the circle: ");
        Scanner s = new Scanner(System.in);
        int r;
        r = s.nextInt();
        double area = Math.PI*r*r;
        double perimeter = 2*Math.PI*r;
        System.out.println("Area of circle: "+area);
        System.out.println("Perimeter of circle: "+perimeter);
    }
    
    Que2(int side) {
        int area = side*side;
        int perimeter = 4*side;
        System.out.println("Area of square: "+area);
        System.out.println("Perimeter of square: "+perimeter);
    }
    
    Que2(int length, int breadth) {
        int area = length*breadth;
        int perimeter = 2*(length+breadth);
        System.out.println("Area of rectangle: "+area);
        System.out.println("Perimeter of rectangle: "+perimeter);
    }
    
    public static void main(String args[]) {
        Que2 obj1 = new Que2();
        Que2 obj2 = new Que2(11);
        Que2 obj3 = new Que2(2,3);
    }
}