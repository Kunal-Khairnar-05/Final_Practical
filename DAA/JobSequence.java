import java.util.*;

public class JobSequence {
    public static void main(String[] args) {
        char[] ids = {'a', 'b', 'c', 'd'};
        int[] profits = {10, 29, 17, 25};
        int[] deadline = {3,2,2,1};

        int n = ids.length;
        int maxD = 3;
        Integer[] idx = {0,1,2,3};

        Arrays.sort(idx, (x,y) -> profits[y] - profits[x]);

        char[] slot = new char[maxD + 1];
        int total=0;
        for(int id: idx){
            for(int t = deadline[id]; t>=1; t--){
                if(slot[t] == '\0'){
                    slot[t] = ids[id];
                    total +=profits[id];
                    break;
                }
            }
        }

        System.out.print("Job Sequence : ");
        for(int i=1; i<=maxD; i++){
            System.out.print(slot[i] + " ");
        }

        System.out.println("\nMax Profit : "+ total);

    }
}