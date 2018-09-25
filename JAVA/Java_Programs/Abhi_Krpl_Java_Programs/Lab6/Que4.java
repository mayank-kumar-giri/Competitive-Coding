public class Que4{
    int n1;
    String n2;
    float n3;
    Que4(int n1,String n2,float n3){
        this.n1=n1;
        this.n2=n2;
        this.n3=n3;
    }
    void display(){System.out.println(n1+" "+n2+" "+n3);}
    
     public static void main(String args[]) {
        Que4 obj = new Que4(2, "Abhishek", 7);
        obj.display();
    }
}