import java.io.*;
import java.util.Scanner;
public class qv
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("\nEnter order of matrix and then the matrix row by row: \n");

        int n = scan.nextInt();
        int[][] arr = new int[n][n];
        int[][] tarr = new int[n][n];
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                arr[i][j] = scan.nextInt();
            }
        }
        
        


        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                tarr[i][j]=arr[j][i];
            }
            
        }


        


        
        int flag=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(tarr[i][j]!=arr[i][j])
                {
                    flag=1;
                    break;
                }
            }
            
        }
        if(flag==0) System.out.print("\nThis is a SYMMETRIC matrix.\n");
        else System.out.print("\nThis is an ASYMMETRIC matrix.\n");
    }   
}