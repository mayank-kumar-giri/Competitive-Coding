import java.util.Scanner;
import java.lang.Math;

public class Que5 {
    
    int id;
    String name;
    
    Que5(int id1, String name1) {
        id = id1;
        name = name1;
    }
    
    Que5(Que5 obj) {
        id = obj.id;
        name = obj.name;
    }
    
    void display() {
        System.out.println("Id is "+id+" and name is "+name);
    }
    
    public static void main(String args[]) {
        Que5 obj = new Que5(1, "Abhishek Kripal");
        obj.display();
    }
}