import java.io.*;
import java.util.Scanner;
public class qiv
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter size of array, position you wanna insert at, element to insert and then elements: \n");
        int n=scan.nextInt(),k=scan.nextInt(),e=scan.nextInt();
        int arr[]=new int[n+1];
        for(int i=0;i<n;i++) arr[i]=scan.nextInt();
        System.out.print("\nYour current array is: \n");
        for(int i=0;i<n;i++) System.out.print(arr[i]+" ");
        System.out.print("\n");
        for(int i=n;i>k-1;i--) arr[i]=arr[i-1];
        arr[k-1]=e;
        System.out.print("\nYour final array is: \n");
        for(int i=0;i<n+1;i++) System.out.print(arr[i]+" ");
    }	
}