import java.io.*;
import java.util.Scanner;
public class qiii
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("\nEnter order of matrix (m & n) of 1st Matrix A and then the matrix row by row: \n");
        int m = scan.nextInt();
        int n = scan.nextInt();
        int[][] a = new int[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                a[i][j] = scan.nextInt();
            }
        }
        System.out.println("\nEnter order of matrix (p & q) of 2nd Matrix B and then the matrix row by row: \n");
        int p = scan.nextInt();
        int q = scan.nextInt();
        if(n==p)
        {
            int[][] b = new int[p][q];
            for(int i=0;i<p;i++)
            {
                for(int j=0;j<q;j++)
                {
                    b[i][j] = scan.nextInt();
                }
            }
            int[][] c = new int[m][q];

            for(int i=0;i<m;i++)
            {
                for(int j=0;j<q;j++)
                {
                    for(int k=0;k<p;k++)
                    {
                        if(k==0) c[i][j]=a[i][k]*b[k][j];
                        else c[i][j]=c[i][j]+a[i][k]*b[k][j];
                    }
                }
            }
            System.out.print("\nProduct matrix: \n");
            for(int i=0;i<m;i++)
            {
                for(int j=0;j<q;j++)
                {
                    System.out.print(c[i][j]+" ");
                }
                System.out.print("\n");
            }
        }
        else
        {
            System.out.print("\nThese 2 matrices CAN'T be multiplied. Invalid orders.\n");
        }   
    }   
}