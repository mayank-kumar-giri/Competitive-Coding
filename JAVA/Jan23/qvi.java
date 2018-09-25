import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
public class qvi
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter size of array and then elements: \n");
        int n=scan.nextInt();
        int arr[]=new int[n];
        int count=0,flag=0;
        for(int i=0;i<n;i++) arr[i]=scan.nextInt();   
        
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(arr[i]>arr[j])
                {
                    count=arr[i];
                    arr[i]=arr[j];
                    arr[j]=count;
                }
            }
        }
        System.out.println("\nThe largest and 2nd largest numbers are: "+arr[n-1]+" & "+arr[n-2]+".\n"); 
        int a=25&35;
        System.out.println(a);
    }
}