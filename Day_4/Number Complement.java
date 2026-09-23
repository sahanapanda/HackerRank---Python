class Solution {
    public int findComplement(int num) {
        // Find the length of the binary string of num
        int bitLength = Integer.toBinaryString(num).length();
        
        // Create a mask with all 1s of the same length
        // For example, if bitLength is 3, mask becomes (1 << 3) - 1 = 8 - 1 = 7 (binary 111)
        int mask = (1 << bitLength) - 1;
        
        // XORing num with the mask flips all its bits
        return num ^ mask;
    }
}
