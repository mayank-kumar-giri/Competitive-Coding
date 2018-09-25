import java.io.*;
import java.util.Scanner;
public class car
{
	static String brand_name = new String("Patanjali");
	int a=2;
	int x=34;
	static
	{
		System.out.print("\nAnd that's called a static block....\n");
	}
	void showbrand()
	{
		System.out.print(brand_name+"\n");
	}
	static void bchange(String b)
	{
		brand_name=b;
	}
	public static void main(String[] args) {
		car cobj = new car();
		cobj.showbrand();
		cobj.bchange("Honeywell");
		cobj.showbrand();
		System.out.print("\n"+cobj.a+" "+cobj.x+"\n");
	}
}