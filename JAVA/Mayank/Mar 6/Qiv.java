import java.io.*;
import java.util.Scanner;
public class Qiv
{
    int a;
    int b;
    Qiv(int a,int b)
    {
        this.a=a;
        this.b=b;
    }
    Qiv(Qiv x)
    {
        a=x.a;
        b=x.b;
    }
    
    void showsum()
    {
        System.out.print((this.a+this.b)+"\n");
    }
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int i1 = scan.nextInt();
        int i2 = scan.nextInt();
        
        
        Qiv obj = new Qiv(i1,i2);
        Qiv obj2 = new Qiv(obj);
        obj.showsum();
        obj2.showsum();
        
    }   
}