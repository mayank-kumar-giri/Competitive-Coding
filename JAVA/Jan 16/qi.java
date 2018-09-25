import java.io.*;
import java.util.Scanner;
public class qi
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	int[] marks = new int[5];
    	System.out.print("Kindly, enter the marks of 5 subjects one by one: \n");
    	int total=0,avg=0,percent=0;
    	for(int i=0;i<5;i++)
    	{
    		marks[i]=scan.nextInt();
    		total=total+marks[i];
    	}
    	avg=total/5;
    	percent=avg;
    	System.out.println("\nThe total marks is "+total+".\nThe average of marks is "+avg+".\nThe student has scored "+percent+"%.\n");
    }	
}