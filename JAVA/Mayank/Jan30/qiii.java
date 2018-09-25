import java.io.*;
import java.util.Scanner;
public class Qiii
{
    Qiii(int a,int b)
    {
        System.out.print("\nsum of Integers"+(a+b)+" \n");
    }
    Qiii(float a,float b)
    {
        System.out.print("\nsum of Integers"+(a+b)+" \n");
    }
    Qiii(double a,double b)
    {
        System.out.print("\nsum of Integers"+(a+b)+" \n");
    }
    Qiii(String a,String b)
    {
        System.out.print("\nsum of Integers"+(a+b)+" \n");
    }
    
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        double d1 = scan.nextDouble();
        double d2 = scan.nextDouble();
        int i1 = scan.nextInt();
        int i2 = scan.nextInt();
        float f1 = scan.nextFloat();
        float f2 = scan.nextFloat();
        String s1 = scan.next();
        String s2 = scan.next();
        
        
        Qii obj = new Qii(d1,d2);
        Qii obj = new Qii(i1,i2);
        Qii obj = new Qii(f1,f2);
        Qii obj = new Qii(s1,s2);
        
    }   
}