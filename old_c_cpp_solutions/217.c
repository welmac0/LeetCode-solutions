bool containsDuplicate(int* nums, int numsSize) {
    int i, j;
    bool swapped;
    for (i = 0; i < numsSize - 1; i++) {
        swapped = false;
        for (j = 0; j < numsSize - 1 - i; j++) {
            if (nums[j] == nums[j+1])
                return 1;
            else if (nums[j] > nums[j+1]) {
                int temp = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = temp;
                swapped = true;
            }
        }

        if (!swapped) break;
    }

    return 0;
}

// 5ms, beats 91.42%
