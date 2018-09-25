import java.util.Scanner;

public class Que3 {
    public static void main(String args[]) {
        int a[][] = new int[10][10];
        int b[][] = new int[10][10];
        int res[][] = new int[10][10];
        int n,i,j,k;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of matrix: ");
        n = scanner.nextInt();
        System.out.println("Enter elements of A matrix: ");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.print("Enter element of A"+"["+i+"]"+"["+j+"] index");
                a[i][j] = scanner.nextInt();
            }
        }
        System.out.println("Enter elements of B matrix: ");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.print("Enter element of B"+"["+i+"]"+"["+j+"] index");
                b[i][j] = scanner.nextInt();
            }
        }
        System.out.println("The resultant matrix is");
        for (i=0;i<n;i++)
        {
            for (j = 0;j<n;j++)
            {
                for (k=0;k<n;k++)
                {
                    res[i][j] = res[i][j] + a[i][k] * b[k][j];
                }
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.print(res[i][j]+" ");
            }
            System.out.println();
        }
        
    }
}