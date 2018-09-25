import java.io.*;
import java.util.Scanner;

abstract class shape
{
	String shape_type;
	abstract void area();
    void moveto(int p1,int p2)
    {
    	System.out.print("\nThis shape is a: "+shape_type);
    	System.out.print("\nParameter-1 is: "+p1);
    	System.out.print("\nParameter-1 is: "+p2);
    }
}

class circle extends shape
{
	int r;
	circle(int r,String s)
	{
		this.r=r;
		shape_type=s;
		System.out.print("\nCONSTRUCTOR of circle has been called...\n");
	}
	void area()
	{
		double ar=3.14*r*r;
		System.out.print("\nArea of circle is: "+ar);

	}
}

class rectangle extends shape
{
	int a,b;
	rectangle(int a,int b,String s)
	{
		this.a=a;
		this.b=b;
		shape_type=s;
		System.out.print("\nCONSTRUCTOR of rectangle has been called...\n");
	}
	void area()
	{
		double ar=a*b;
		System.out.print("\nArea of rectangle is: "+ar);
	}
}

public class q2
{
	public static void main(String[] args) 
	{
		circle c = new circle(2,"circle");
		rectangle r = new rectangle(3,6,"rectangle");
		c.area();
		r.area();
		c.moveto(100,111);
		r.moveto(05,50);		
	}
}