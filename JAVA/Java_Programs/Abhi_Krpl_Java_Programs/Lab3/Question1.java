import java.util.Scanner;

public class Question1 {
    public static void main(String args[]) {
        int n1,n2,flag=0,i,j;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a lower range: ");
        n1 = scanner.nextInt();
        System.out.print("Enter a higher limit: ");
        n2 = scanner.nextInt();
        System.out.println("The prime number between the range are");
        for(i=n1;i<=n2;i++)
        {
            for(j=2;j<i;j++)
            {
                if(i%j==0)
                {
                    flag=0;
                    break;
                }
                else
                {
                    flag=1;
                }
            }
            if(flag==1)
            {System.out.println(i);}
        }
    }
}