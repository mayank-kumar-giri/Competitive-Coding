import java.util.Scanner;

public class Que1 {
    public static void main(String args[]) {
        int arr[] = new int[10];
        int n,i;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of elements in array: ");
        n = scanner.nextInt();
        System.out.print("Enter elements of array: ");
        for(i=0;i<n;i++)
        {
            arr[i] = scanner.nextInt();
        }
        int largest=arr[0],smallest=arr[0];
        for(i=0;i<n;i++)
        {
            if(largest<arr[i])
            {largest=arr[i];}
            if(smallest>arr[i])
            {smallest=arr[i];}
        }
        System.out.println("The smallest and largest elements are: "+smallest+" "+largest);
        
    }
}