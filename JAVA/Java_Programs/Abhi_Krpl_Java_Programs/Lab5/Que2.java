import java.io.*;
import java.util.Scanner;

class Circle{
	double r;
}

class Rectangle {
	double l;
	double b;
}

class Square {
	double a;
}

class Triangle {
	double base;
	double height;

}

class Que2 {
	public static void main(String args[]){

		Circle c = new Circle();
		Rectangle r = new Rectangle();
		Square s = new Square();
		Triangle t = new Triangle();

		Scanner scanner = new Scanner(System.in);
		System.out.print("Radius of Circle");
		c.r = scanner.nextDouble();
		System.out.print("Length of rectangle");
		r.l = scanner.nextDouble();
		System.out.print("Breadth of rectangle");
		r.b = scanner.nextDouble();
		System.out.print("Side");
		s.a = scanner.nextDouble();
		System.out.print("Base of triangle");
		t.base = scanner.nextDouble();
		System.out.print("Height of triangle");
		t.height =scanner.nextDouble();
        
		double area_c = 3.14*c.r*c.r;
		double peri_c = 3.14*2*c.r;
		double area_r = r.l*r.b;
		double peri_r = 2*(r.l+r.b);
		double area_s = s.a*s.a;
		double peri_s = 4*s.a;
		double area_t = 0.5*(t.height+t.base);


		System.out.println("Area of circle:" + area_c);
		System.out.println("Area of rectangle:" + area_r);
		System.out.println("Area of square:" + area_s);
		System.out.println("Area of triangle:" + area_t);
		System.out.println("Perimeter of circle:" + peri_c);
		System.out.println("Perimeter of rectangle:" + peri_r);
		System.out.println("Perimeter of square:" + peri_s);



	}
}