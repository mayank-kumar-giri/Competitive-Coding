class Lab5
{
public static void main (String args[])
{
    int a = Integer.parseInt(args[0]);
    double res, res1;
    res = 3.1415*a*a;
    res1 = 2*3.1415*a;
    System.out.println("Area: " +res);
    System.out.println("Perimeter: " +res1);
}
}