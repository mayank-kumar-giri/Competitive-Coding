import java.util.Scanner;

public class EmployeeDetails {
    
    private String name;
    private int age;
    private String designation;
    
    public String getName() {
        return name;
    }
    
    public String getDesignation() {
        return designation;
    }
    
    public int getAge() {
        return age;
    }
    
    
    void display() {
        System.out.println("Name: "+name+"\nAge: "+age+"\nDesignation: "+designation);
    }
    
    
    public static void main(String args[]) {
        EmployeeDetails obj = new EmployeeDetails();
        obj.name = "Abhishek Kripal";
        obj.age = 19;
        obj.designation = "Django developer";
        obj.display();
        int age1;
        age1 = obj.getAge();
        System.out.println("Accessing age with method: "+age1);
    }
}