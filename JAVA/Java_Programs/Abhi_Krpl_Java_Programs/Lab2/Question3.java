import java.util.Scanner;

public class Question3 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char ch;
        ch = scanner.next().charAt(0);
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U')
        {System.out.println("Character "+ch+" is vowel");}
        else
        {System.out.println("Character is not vowel.");}
    }
}