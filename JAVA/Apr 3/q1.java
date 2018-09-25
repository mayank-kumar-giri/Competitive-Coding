import java.io.*;
import java.util.Scanner;

abstract class vehicle
{
	abstract void number_of_wheels();
}

class car extends vehicle
{
	void number_of_wheels()
	{
		System.out.print("\n4\n");
	}
}

class bus extends vehicle
{
	void number_of_wheels()
	{
		System.out.print("\n6\n");
	}
}

class bike extends vehicle
{
	void number_of_wheels()
	{
		System.out.print("\n2\n");
	}
}

public class q1
{
	int a=10;
	public static void main(String[] args) 
	{
		car c = new car();
		bus b = new bus();
		bike bi = new bike();
		c.number_of_wheels();
		b.number_of_wheels();
		bi.number_of_wheels();
	}
}