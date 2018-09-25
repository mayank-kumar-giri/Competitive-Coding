import java.util.Scanner;

class Que4 {
    
    private static String name="Abhishek";
    private static int age=19;
    private static String designation="Django developer";
    
    
    public static class Que4_inner {
        public static void display_inner() {
            System.out.println("Name: "+name+"\nAge: "+age+"\nDesignation: "+designation);
        }
    }
    
    public static void display() {
        System.out.println("Name: "+name+"\nAge: "+age+"\nDesignation: "+designation);
    }
    
    
    public static void main(String args[]) {
        Que4 obj1 = new Que4();
        Que4.Que4_inner x = new Que4.Que4_inner();
        x.display_inner();
    }
}