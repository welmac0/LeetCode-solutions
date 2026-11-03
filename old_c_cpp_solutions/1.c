int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    for (i = 0; i < numsSize; i++) {
        for (j = i+1; j < numsSize; j++) {
            if (i != j) {
                if (nums[i] + nums[j] == target) {
                    int *new_tab = malloc(2*sizeof(int));
                    new_tab[0] = i;
                    new_tab[1] = j;
                    *returnSize = 2;
                    return new_tab;
                }
            }
        }
    }
    *returnSize = 2;
    return NULL;
}
