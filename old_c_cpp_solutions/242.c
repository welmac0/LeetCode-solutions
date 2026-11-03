bool isAnagram(char* s, char* t) {
    int lens, lent;
    for (lens = 0; s[lens] != '\0'; lens++);
    for (lent = 0; t[lent] != '\0'; lent++);
    if (lens!=lent) return 0;

    int counter_s[256] = {0}, counter_t[256] = {0}, i;

    for (i = 0; s[i] != '\0'; i++) {
        counter_s[s[i]] += 1;
        counter_t[t[i]] += 1;
    }

    for (i = 0; i < 256; i++)
        if (counter_s[i] != counter_t[i]) return 0;

    return 1;
} // 0ms, beats 100%
