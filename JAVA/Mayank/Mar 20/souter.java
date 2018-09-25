import java.io.*;
import java.util.Scanner;
public class souter
{
	private static int salary_of_outer;
	souter(int s)
	{
		salary_of_outer=s;
	}
	static void show_salary()
	{
		System.out.print("\nSalary of outer is : "+salary_of_outer+"\n");
	}
	public static class inner
	{
		static int salary_of_inner;
		inner(int s)
		{
			salary_of_inner=s;
		}
		static void add_salary_of_outer_to_inner()
		{
			salary_of_inner+=salary_of_outer;
		}
		static void show_salary()
	    {
			System.out.print("\nSalary of inner is : "+salary_of_inner+"\n");
		}

	}
	public static void main(String[] args) 
	{
		outer oo = new outer(25000);
		outer.inner io = oo.new inner(10000);
		io.show_salary();
		io.add_salary_of_outer_to_inner();
		io.show_salary();
		oo.show_salary();
	}
}