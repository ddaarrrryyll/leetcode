

int search(int* nums, int numsSize, int target){
    if (!nums || numsSize == 0) return 0;
    
    int head = 0;
    int tail = numsSize - 1;
    int mid, start;    
    
    // BS for smallest e
    while (head < tail) {
        mid = head + (tail - head) / 2;
        // printf("mid %d\n", mid);
        if (nums[mid] > nums[tail]) head = mid + 1;
        else tail = mid;
    }
    
    start = head;
    head = 0;
    tail = numsSize - 1;
    
    printf("head %d, tail %d, target %d start %d\n", nums[head], nums[tail], target, start);
    
    if ((target >= nums[start]) && (target <= nums[tail])) head = start;
    else tail = start;
    
    // BS for target
    while (head <= tail) {
        if (target == nums[head]) return head;
        else if (target == nums[tail]) return tail;
        
        mid = head + (tail - head) / 2;
        printf("head %d, tail %d, mid %d\n", nums[head], nums[tail], nums[mid]);
        if (nums[mid] == target) return mid;
        else {
            if (nums[mid] < target) head = mid + 1;
            else tail = mid - 1;
        }
    }
    return -1;
}