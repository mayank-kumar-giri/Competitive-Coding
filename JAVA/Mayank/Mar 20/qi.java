import java.io.*;
import java.util.Scanner;
public class car
{
	static String brand_name = new String("Patanjali");
	int a=2;
	float b=3.2;
	static
	{
		System.out.print("\nAnd that's called a static block....\n");
	}
	static void bchange()
	{
		brand_name="Mera apna brand";
		System.out.print(brand_name+"\n");
	}
	public static void main(String[] args) {
		car cobj = new car();
		cobj.bchange();
		System.out.print("\n"+cobj.a+" "+cobj.b+"\n");
	}
}