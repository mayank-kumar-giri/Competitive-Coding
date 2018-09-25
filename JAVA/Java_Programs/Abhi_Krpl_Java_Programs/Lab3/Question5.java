import java.util.Scanner;

public class Question5 {
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
        int[] temp = new int[n];
        int j=0;
        for(i=0;i<n-1;i++)
        {
            if(arr[i]!=arr[i+1]) {
                temp[j++] = arr[i];
            }
        }
        temp[j++] = arr[n-1];
        for(i=0;i<j;i++) {
            arr[i] = temp[i];
        }
        System.out.println("Array after removing duplicate elements are: ");
        for(i=0;i<n;i++)
        {System.out.println(temp[i]);}
        
    }
}