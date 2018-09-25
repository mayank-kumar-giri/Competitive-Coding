import java.util.Scanner;

public class Question4 {
public static void main(String args[]) {
Scanner scanner = new Scanner(System.in);
System.out.print("Enter 3 numbers: ");
int a,b,c;
a = scanner.nextInt();
b = scanner.nextInt();
c = scanner.nextInt();
if(a>b) {
    if(a>c)
    {System.out.println("Largest: "+a);}
    else
    {System.out.println("Largest: "+c);}
}
    else {
        if(b>c)
        {System.out.println("Largest: "+b);}
        else
        {System.out.println("Largest: "+c);}
    }
    
}
}