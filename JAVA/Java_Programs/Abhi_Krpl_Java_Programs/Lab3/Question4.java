import java.util.Scanner;

public class Question4 {
    public static void main(String args[]) {
        int i,j,n,pos;
        int arr[] = new int[10];
        System.out.print("Enter element: ");
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        System.out.print("Enter a index to insert the element in array: ");
        pos = scanner.nextInt();
        arr[pos] = n;
        for(i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+" ");
        }
    }
}