import java.util.Scanner;

public class Question6 {
    public static void main(String args[]) {
        int a[] = new int[10];
        int n,i,j;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of elements in array: ");
        n = scanner.nextInt();
        System.out.print("Enter elements of array: ");
        for(i=0;i<n;i++)
        {
            a[i] = scanner.nextInt();
        }
        
       int temp;
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                {
                    temp=a[i];
                    a[i]=a[j];
                    a[j]=temp;
                }
            }
        }
        System.out.println("Second largest: "+a[n-2]);
        
    }
}