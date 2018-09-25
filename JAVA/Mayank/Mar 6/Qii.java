import java.io.*;
import java.util.Scanner;
public class Qii
{
    double r;
    double a;
    double b;
    Qii(double r,double a,double b)
    {
        this.r=r;
        this.a=a;
        this.b=b;
    }
    void perimeter()
    {
        double c,s,r;
        c=2*3.14*this.r;
        s=4*this.a;
        r=2*(this.a+this.b);
        System.out.print("\nThe perimeters are as follows:\nCircle "+c+"\nSquare "+s+"\nRectangle "+r+"\n");
    }
    void area()
    {
        double cp,sp,rp;
        cp=3.14*r*r;
        sp=a*a;
        rp=a*b;
        System.out.print("\nThe areas are as follows:\nCircle "+cp+"\nSquare "+sp+"\nRectangle "+rp+"\n");

    }
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        double r = scan.nextDouble();
        double a = scan.nextDouble();
        double b = scan.nextDouble();
        
        Qii obj = new Qii(r,a,b);
        obj.perimeter();
        obj.area();        
    }   
}