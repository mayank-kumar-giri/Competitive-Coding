import java.util.Scanner;

public class Car {
    
    static String brand_name;
    
    Car(String name1) {
        brand_name = name1;
    }
    
    
    void display() {
        System.out.println("Brand name is "+brand_name);
    }
    
    static void new_Brand() {
        Scanner s = new Scanner(System.in);
        String ns;
        System.out.print("Enter a new brand to update: ");
        ns = s.next();
        brand_name = ns;
    }
    
    public static void main(String args[]) {
        Car obj = new Car("Lamborghini");
        obj.display();
        obj.new_Brand();
        obj.display();
    }
}