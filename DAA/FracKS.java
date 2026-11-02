import java.util.*;

public class FracKS {
    public static void main(String[] args) {
        int[] w = {10,20,30};
        int[] p = {60,100,120};
        int cap = 50;

        Integer[] idx = {0,1,2};

        Arrays.sort(idx, (x,y)-> Double.compare(p[y]/w[y], p[x]/w[x]));

        double total = 0;

        for(int i: idx){
            if(cap>=w[i]){
                cap -= w[i];
                total+=p[i];
            }
            else{
                total+=p[i] * ((double) cap / w[i]);
                break;
            }
        }

        System.out.println("Maximum value: " + total);
    }
}
