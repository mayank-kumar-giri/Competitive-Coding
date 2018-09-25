import java.io.*;
import java.util.Scanner;
public class qii
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter n: \n");
        int n = scan.nextInt();
        int[] fibo = new int[n];
        int count=2,i=2,sum=1;
        fibo[0]=0;
        fibo[1]=1;
        System.out.print("\nThe n terms of Fibonacci series are as follows: \n");
        System.out.print(fibo[0]+" "+fibo[1]+" ");
        while(count!=n)
        {
            fibo[i]=fibo[i-1]+fibo[i-2];
            System.out.print(fibo[i]+" ");
            sum=sum+fibo[i];
            count++;
            i++;
        }
        System.out.print("\nAnd the sum of these terms is: "+sum+".");
    }	
}