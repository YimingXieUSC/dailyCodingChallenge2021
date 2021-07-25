import java.util.Arrays;

class Solution {
    public int[] solution(int[] A, int F, int M){
        int[] answer = new int[F];
        int leftOvers = M * (A.length + F); 
        for(int i = 0; i < A.length; i++){
            leftOvers -= A[i];
        }
        if((leftOvers / F) > 6){
           answer = new int[]{0};
           return answer;
        }
       else{
            Arrays.fill(answer, 1);
           int modResults = leftOvers % F;
           int index = 0;
           while(modResults != 0){
              answer[index] += 1;
              modResults--;
              index = index + 1 % F; 
            }
            return answer;
       }  
    }
}
