import java.util.Scanner;

public class Que3 {
    
    private String name="Abhishek";
    private int age=19;
    private String designation="Django developer";
    
    public String getName() {
        return name;
    }
    
    public String getDesignation() {
        return designation;
    }
    
    public int getAge() {
        return age;
    }
    
    public class Que3_inner {
        public void display_inner() {
            System.out.println("Name: "+name+"\nAge: "+age+"\nDesignation: "+designation);
        }
    }
    
    void display() {
        System.out.println("Name: "+name+"\nAge: "+age+"\nDesignation: "+designation);
    }
    
    
    public static void main(String args[]) {
        Que3 obj1 = new Que3();
        Que3.Que3_inner x = obj1.new Que3_inner();
        int age1;
        age1 = obj1.getAge();
        System.out.println("Accessing age with method: "+age1);
    }
}