// the idea is to remove last digit for if it's even until it is odd and because of inputs greater than
// longlong ie("32782489638346578713315098393010310518347382"), we cannot convert input to an integer

char * largestOddNumber(char * num){
    int a = num[strlen(num) - 1] - '0';
    while ((a % 2 == 0) && num[0] != NULL) {
        num[strlen(num) - 1] = '\0';
        if (num[0] != NULL) a = num[strlen(num) - 1] - '0';
        // printf("in loop %d num %s\n", a, num);
    }
    // printf("ans %s\n", num);
    return num;
}