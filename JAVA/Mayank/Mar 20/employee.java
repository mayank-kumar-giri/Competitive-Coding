import java.io.*;
import java.util.Scanner;
public class employee
{
	private String name = new String("Name");
	private int salary;
	private int age;

	employee(String name,int salary,int age)
	{
		this.name=name;
		this.age=age;
		this.salary=salary;
	}

	void amplify_the_salary(int factor)
	{
		salary*=factor;
	}

	void show_salary()
	{
		System.out.print("\nSalary of employee "+name+" is : "+salary+"\n");
	}
	
	void increment_age()
	{
		age++;
	}

	void show_age()
	{
		System.out.print("\nAge of employee "+name+" is : "+age+"\n");
	}


	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		System.out.print("\nEnter name, salary and age of the employee: \n");
		String name = scan.next();
	    int salary = scan.nextInt();
	    int age = scan.nextInt();
		
		employee e1 = new employee(name,salary,age);
		e1.show_salary();
		e1.amplify_the_salary(2);
		e1.show_salary();
		e1.amplify_the_salary(10);
		e1.show_salary();
		e1.show_age();
		e1.increment_age();
		e1.show_age();
	}
}