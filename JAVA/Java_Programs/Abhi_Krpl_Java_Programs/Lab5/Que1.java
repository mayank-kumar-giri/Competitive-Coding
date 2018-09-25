import java.io.*;
public class Que1 {

   public String name;

   public Que1 (String Name) {
      name = Name;
   }
   public void printEmp() {
      System.out.println("name  : " + name );
   }

   public static void main(String args[]) {
      Que1 emp = new Que1("Abhishek");
      emp.printEmp();
   }
}