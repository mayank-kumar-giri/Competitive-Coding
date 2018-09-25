import java.util.Scanner;

public class Question1 {
public static void main(String args[]) {
Scanner scanner = new Scanner(System.in);
System.out.print("Enter the marks of 5 subjects: ");
int a[];
a = new int[5];
for(int i=0;i<5;i++)
{
a[i] = scanner.nextInt();
}
float avg;
avg = (a[0]+a[1]+a[2]+a[3]+a[4])/5;
System.out.println("The average is "+avg);
System.out.println("The percentage is "+avg +"%");
}
}