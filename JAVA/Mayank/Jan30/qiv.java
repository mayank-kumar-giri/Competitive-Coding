import java.io.*;
import java.util.Scanner;
public class Qiii
{
    int a;
    int b;
    Qiii(int a,int b)
    {
        this.a=a;
        this.b=b;
    }
    Qiii(Qiii x)
    {
        a=c.a;
        b=c.b;
    }
    
    void showsum()
    {
        System.out.print((this.a+this.b));
    }
    
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int i1 = scan.nextInt();
        int i2 = scan.nextInt();
        
        
        Qiv obj = new Qiii(i1,i2);
        Qiv obj2 = new Qiii(obj);
        obj.showsum();
        obj2.showsum();
        
    }   
}