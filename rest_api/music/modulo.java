import java.util.*;
class modulo{
static int i;
static long q;
static long modulo(long  k, long a){
    long  m=1000000007; i++;
    System.out.println(i+" k = "+k+" a = "+q);
    System.out.println("Bhar wala a = "+a);
    if(k==0)
        return 1;

    if(k%2!=0){
        q=a;
        return (a*modulo((k-1)/2,((a*a)%m)))%m;
    }    
    return modulo(k/2,((a*a)%m));
}
    public static void main(String[]args){
        long  t,k,m=1000000007;
        Scanner sc=new Scanner(System.in);
        t=sc.nextLong();
        while(t-->0){
            k=sc.nextLong();
            System.out.println("In for loop");
            for(int j =0 ;j<(int)k;j++){
                System.out.println((j+1)+" k = "+Math.pow(2,j+1));
            }
            System.out.println("In recursive function ");
    	    long  a = modulo(k-1,2);
    	    System.out.println(a);
            a=a*10;
    	    a=a%m;
    	    System.out.println(a);
        }
    }
}