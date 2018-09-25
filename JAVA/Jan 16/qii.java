import java.io.*;
import java.util.Scanner;
import java.lang.Math;
public class qii
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	double[] sides = new double[3];
    	System.out.print("Kindly, enter the 3 sides of the triangle one by one: \n");
    	double area=0,s=0;
    	for(int i=0;i<3;i++)
    	{
    		sides[i]=scan.nextDouble();
    		s=s+sides[i];
    	}
    	s=s/2;
        area=Math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]));
    	System.out.println("\nThe area of the triangle is "+area+".\n");
    }	
}