import java.io.*;
import java.util.Scanner;

interface shape
{
	void area();
}

class circle implements shape
{
	int r;
	circle(int r)
	{
		this.r=r;
		System.out.print("\nCONSTRUCTOR of circle has been called...\n");
	}
	public void area()
	{
		double ar=3.14*r*r;
		System.out.print("\nArea of circle is: "+ar);

	}
}

class rectangle implements shape
{
	int a,b;
	rectangle(int a,int b)
	{
		this.a=a;
		this.b=b;
		System.out.print("\nCONSTRUCTOR of rectangle has been called...\n");
	}
	public void area()
	{
		double ar=a*b;
		System.out.print("\nArea of rectangle is: "+ar);
	}
}

public class q3
{
	public static void main(String[] args) 
	{
		circle c = new circle(2);
		rectangle r = new rectangle(3,6);
		c.area();
		r.area();		
	}
}