import java.io.*;
import java.util.Scanner;
public class qiii
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
        int count=0,flag=0;
        System.out.print("\n");
        while(true)
        {
            if(count<=7 && flag==0)
            {
                for(int i=1;i<=count;i++)
                {
                    System.out.print(i+" ");
                }
                System.out.print("\n");
                count++;
            }
            else
            {
                if(count==8)
                {
                    count=6;
                    flag=1;
                }
                for(int i=1;i<=count;i++)
                {
                    System.out.print(i+" ");
                }
                System.out.print("\n");
                count--;
            }
            if(count==0 && flag==1) break;
        }
    }	
}