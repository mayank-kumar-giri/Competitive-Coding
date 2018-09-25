import java.util.Scanner;

public class Que5 {
    public static void main(String args[]) {
        int n,i,j,r,c,count=0;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter rows and columns of matrix: ");
        r = scanner.nextInt();
        c = scanner.nextInt();
        int a[][] = new int[r][c];
        int t[][] = new int[c][r];

        System.out.println("Enter elements of A matrix: ");
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                System.out.print("Enter element of A"+"["+i+"]"+"["+j+"] index");
                a[i][j] = scanner.nextInt();
            }
        }
        System.out.println("Your entered matrix is");
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                System.out.print(a[i][j]+" ");
                t[i][j]=a[j][i];
            }
            System.out.println();
        }
        for(i=0;i<c;i++)
        {
            for(j=0;j<r;j++)
            {
                t[i][j]=a[j][i];
            }
            System.out.println();
        }
        
        System.out.println("The transpose matrix is");
        for(i=0;i<c;i++)
        {
            for(j=0;j<r;j++)
            {
                System.out.print(t[i][j]+" ");
            }
            System.out.println();
        }
        if(r==c)
        {
            for(i=0;i<c;i++)
            {
                for(j=0;j<r;j++)
                {
                    if(a[i][j]==t[i][j])
                    {count++;}
                }
            }
            if(count==(r*c))
            {System.out.println("It is a symmetric matrix");}
            else
                System.out.println("It is not a symmetric matrix");
        }
        else
        {
            System.out.println("It is not a symmetric matrix");
        }
    }
}