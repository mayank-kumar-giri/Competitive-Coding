import java.util.Scanner;

public class Que4 {
    public static void main(String args[]) {
        int a[][] = new int[10][10];
        int n=3,i,j,res;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter elements of A matrix: ");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.print("Enter element of A"+"["+i+"]"+"["+j+"] index");
                a[i][j] = scanner.nextInt();
            }
        }
        System.out.println("Your entered matrix is");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
        res = a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1]) -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0]) + a[0][2]*(a[1][0]*a[2][1]-a[2][0]*a[1][1]);
        System.out.println("Determinant value is: "+res);
        
    }
}