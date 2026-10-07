import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        // Total elements in an n-bit sequence is 2^n
        int numElements = 1 << n; 
        
        for (int i = 0; i < numElements; i++) {
            // Apply the standard binary-to-gray conversion formula
            result.add(i ^ (i >> 1));
        }
        
        return result;
    }
}
