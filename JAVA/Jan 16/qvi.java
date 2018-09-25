import java.io.*;
import java.util.Scanner;
public class qvi
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.print("Kindly, enter the number: \n");
        int n = scan.nextInt();
        int sum=0,cd=0;
        for(int i=0;i<3;i++)
        {
            cd=n%10;
            sum+=cd;
            n/=10;
        }
        System.out.println("\nThe sum of digits of this number is "+sum+".\n");
    }   
}