import java.io.*;
import java.util.Scanner;
import java.lang.Math;
public class qv
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.print("Kindly, enter the number: \n");
    	int n=scan.nextInt();
        if(n>0)
        {
            System.out.println("\nPositive.\n");
        }
    	else if(n==0)
        {
            System.out.println("\nZero.\n");
        }
        else
        {
            System.out.println("\nNegative.\n");
        }
    }	
}