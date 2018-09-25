import java.io.*;
import java.util.Scanner;
public class Qii
{
    float r;
    float a;
    float b;
    Qii(float r,float a,float b)
    {
        this.r=r;
        this.a=a;
        this.a=b;
    }
    float perimeter()
    {
        float cp,sp,rp;
        cp=2*3.14*r;
        sp=4*a;
        rp=2*(a+b);
        System.out.print("\nThe perimeters are as follows:\nCircle "+cp+"\nSquare "+sp+"\nRectangle "+rp+"\n");
    }
    float area()
    {
        float cp,sp,rp;
        cp=3.14*r*r;
        sp=a*a;
        rp=a*b;
        System.out.print("\nThe areas are as follows:\nCircle "+cp+"\nSquare "+sp+"\nRectangle "+rp+"\n");
    }
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        Qii obj = new Qii(scan.nextInt(),scan.nextInt(),scan.nextInt());
        obj.perimeter();
        obj.area();        
    }   
}