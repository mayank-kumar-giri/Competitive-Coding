import java.io.*;
import java.util.Scanner;
public class qi
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter n: \n");
        int n = scan.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++) arr[i]=scan.nextInt();
        for(int i=1;i<n;i++)
        {
            if(arr[0]>arr[i])
            {
                int temp=arr[0];
                arr[0]=arr[i];
                arr[i]=temp;
            }
        }
        System.out.print("\nSmallest number is: "+arr[0]+" \n");
        for(int i=1;i<n;i++)
        {
            if(arr[0]<arr[i])
            {
                int temp=arr[0];
                arr[0]=arr[i];
                arr[i]=temp;
            }
        }
        System.out.print("\nLargest number is: "+arr[0]+" \n");
    }	
}