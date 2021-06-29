

int longestOnes(int* nums, int numsSize, int k){
    // sliding window
    // [1,1,1,0,0,0,1,1,1,1,0]
    //            j   
    //                      i
    int i = 0;
    int j = 0;
    
    while (i < numsSize) {
        // decrement k to 'convert' 0 to 1
        if (nums[i] == 0) k--;
        // if k < 0 we need to move j
        if (k < 0) {
            if (nums[j] == 0) k++;
            j++;
        }
        i++;
        // i and j is moved together if k < 0 to keep the biggest i - j  value
        // printf("i = %d, j = %d, k = %d\n", i, j, k);
    }
    return i - j;
}