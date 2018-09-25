import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
public class qv
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter size of array and then elements: \n");
        int n=scan.nextInt();
        int arr[]=new int[n];
        int count=0,flag=0;
        for(int i=0;i<n;i++) arr[i]=scan.nextInt();   
        System.out.print("\nYour current array is: \n");
        for(int i=0;i<n;i++) System.out.print(arr[i]+" ");     
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(arr[j]==arr[i])
                {
                    for(int k=j;k<(n-1);k++) arr[k]=arr[k+1];
                    arr[n-1]=0;
                    n=n-1;
                    flag=1;
                }
            }
            if(flag==1)
            {
                i=i-1;
                flag=0;
                continue;
            }         
        }

        System.out.print("\nYour final array is: \n");
        for(int i=0;i<n;i++) System.out.print(arr[i]+" ");
    }	
}