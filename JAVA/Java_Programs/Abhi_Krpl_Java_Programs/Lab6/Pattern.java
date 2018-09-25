import java.util.Scanner
class Pattern{
 int i,n,j;    
 public static void main()
 {
 Scanner number = new Scanner(System.in)
 System.out.print("Enter the number of times you want to print");
 int rows = number.nextInt();
 for(i=1;i<n;i++)
 {
  for(j=i;j<rows;j++)
  {
   System.out.println("*")
  }
 }
 }    
}