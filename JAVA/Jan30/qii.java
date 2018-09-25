import java.io.*;
import java.util.Scanner;
public class qii
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.println("\nEnter order of matrix (m & n) and then the matrix row by row: \n");
        int m = scan.nextInt();
        int n = scan.nextInt();
        int[][] arr = new int[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                arr[i][j] = scan.nextInt();
            }
        }
        System.out.print("\nCurrent matrix: \n");
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                System.out.print(arr[i][j]+" ");
            }
            System.out.print("\n");
        }
        System.out.print("\nTranspose matrix: \n");
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                System.out.print(arr[j][i]+" ");
            }
            System.out.print("\n");
        }
    }	
}