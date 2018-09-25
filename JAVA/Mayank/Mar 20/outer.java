import java.io.*;
import java.util.Scanner;
public class outer
{
	private int salary_of_outer;
	outer(int s)
	{
		salary_of_outer=s;
	}
	void show_salary()
	{
		System.out.print("\nSalary of outer is : "+salary_of_outer+"\n");
	}
	public class inner
	{
		int salary_of_inner;
		inner(int s)
		{
			salary_of_inner=s;
		}
		void add_salary_of_outer_to_inner()
		{
			salary_of_inner+=salary_of_outer;
		}
		void show_salary()
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