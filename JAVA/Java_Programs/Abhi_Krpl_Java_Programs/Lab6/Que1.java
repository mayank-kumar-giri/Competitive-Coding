import java.util.Scanner;

public class Que1 {
    
    Que1() {
        System.out.println("Default");
    }
    
    public void custom() {
        System.out.println("Custom method");
    }
    
    public static void main(String args[]) {
        Que1 obj = new Que1();
        obj.custom();
    }
}