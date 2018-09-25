import java.io.*;
import java.util.Scanner;
public class qi
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	int[] range = new int[2];
    	System.out.println("\nEnter the lower and upper limits of your range: \n");
        range[0]=scan.nextInt();
        range[1]=scan.nextInt();
        int flag=0;
        System.out.println("\nThe prime numbers in this range are: \n");
        if(range[0]<=2) System.out.print("2 ");
        for(int i=range[0];i<=range[1];i++)
        {
            for(int j=i-1;j>1;j--)
            {
                if(i%j==0) break;
                if(i%j!=0 && j==2)
                {
                    flag=1;
                }
            }
            if(flag==1)
            {
                System.out.print(i+" ");
                flag=0;
            }
        }
    }	
}