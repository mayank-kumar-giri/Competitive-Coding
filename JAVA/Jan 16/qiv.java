import java.io.*;
import java.util.Scanner;
import java.lang.Math;
public class qiv
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	double[] nos = new double[3];
        System.out.print("Kindly, enter the 3 numbers one by one: \n");
        for(int i=0;i<3;i++)
        {
            nos[i]=scan.nextDouble();
        }
        if(nos[0]>nos[1])
        {
            if(nos[0]>nos[2]) System.out.println("\nLargest is "+nos[0]+".\n");
            else System.out.println("\nLargest is "+nos[2]+".\n");
        }
    	else
        {
            if(nos[1]>nos[2]) System.out.println("\nLargest is "+nos[1]+".\n");
            else System.out.println("\nLargest is "+nos[2]+".\n");
        }
    }	
}