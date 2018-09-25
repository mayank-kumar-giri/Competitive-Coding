import java.io.*;
import java.util.Scanner;

class Sum {
	void sum(int arr[],int l)
    {
		int i,sum=0;
		for(i=0;i<l;i++){
			sum=sum+arr[i];
		}
		System.out.println("Sum=" +sum);
	}
}
class Que3{
	public static void main(String args[]){
		Scanner scan= new Scanner(System.in);
		int len,i;
		Sum s=new Sum();
		System.out.print("Enter length of array: ");
		len=scan.nextInt();
		int arr[] = new int[len];
		for(i=0;i<len;i++){
            System.out.print("Enter "+(i+1)+" element: ");
			arr[i]=scan.nextInt();
		}
		s.sum(arr,len);
	}
}