import java.util.Scanner;

public class Question2 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n,count=0,i;
        System.out.print("Enter the range of fibonacci: ");
        n = scanner.nextInt();
        int n1=0,n2=1,n3;
        if(n==0)
        {System.out.println(n1); System.out.println(count);}
        else if(n==1)
        {System.out.println(n2); count+=1; System.out.println(count);}
        else
        {
        count+=1;
        System.out.println(n1);
        System.out.println(n2);
        for(i=2;i<n;i++)
        {
            n3 = n1 + n2;
            n1=n2;
            n2=n3;
            System.out.println(n3);
            count += n3;
        }
        System.out.println("Sum of range: "+count);
        }
    }
}