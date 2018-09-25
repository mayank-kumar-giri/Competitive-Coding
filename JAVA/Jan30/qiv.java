import java.io.*;
import java.util.Scanner;
public class qiv
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("\nEnter a 3x3 matrix row by row: \n");
        int[][] a = new int[3][3];
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                a[i][j] = scan.nextInt();
            }
        }
        int d;
        d=a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1]);
        d=d+(-1)*a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0]);
        d=d+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);

        System.out.println("\nThe determinant of this matrix is: "+d+"\n");
    }   
}