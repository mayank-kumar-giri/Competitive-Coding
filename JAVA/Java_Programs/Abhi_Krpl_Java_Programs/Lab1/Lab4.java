class Lab4
{
public static void main (String args[])
{
    int a = Integer.parseInt(args[0]);
    int b = Integer.parseInt(args[1]);
    int c = Integer.parseInt(args[2]);
    int res;
    res = (a>b)?((a>c)?a:c):((b>c)?b:c);
    System.out.println("Largest between 3 number");
    System.out.println("Largest: " +res);
}
}