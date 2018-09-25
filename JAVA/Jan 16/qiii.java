import java.io.*;
import java.util.Scanner;
import java.lang.Math;
public class qiii
{
    public static void main(String[] args)
    {
    	Scanner scan = new Scanner(System.in);
    	System.out.print("Kindly, enter the character: \n");
    	char r=scan.next().charAt(0);
        if(r=='a'||r=='e'||r=='i'||r=='o'||r=='u'||r=='A'||r=='E'||r=='I'||r=='O'||r=='U')
        {
            System.out.println("\nIt's a vowel.\n");
        }
    	else
        {
            System.out.println("\nIt's NOT a vowel.\n");
        }
    }	
}