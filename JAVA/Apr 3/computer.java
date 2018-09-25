import java.io.*;
import java.util.Scanner;

interface software
{
	void type(String p);
}

interface hardware
{
	void component(String q);
}

public class computer implements software,hardware
{
	public void type(String s)
	{
		System.out.print("\nType of software: "+s);
	}
	public void component(String s)
	{
		System.out.print("\nType of hardware component: "+s);
	}
	public static void main(String[] args) 
	{
		Scanner scan = new Scanner(System.in);
		System.out.print("\nEnter the software-type and component-name: \n");	
		String soft = scan.next();
		String comp = scan.next();
		computer c = new computer();
		c.type(soft);
		c.component(comp);
	}
}