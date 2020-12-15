#include <stdio.h>
#include <stdlib.h>


#include <stdio.h>
#include <stdlib.h>

#define true 1
#define false 0

int f[30000000];
//6,3,15,13,1,0
int main(int argc, char **argv) {

    int idx = atoi(argv[1]);

    for (int i=0; i<30000000; i++) {
        f[i] = -1;
    }

    // hardcoded the input
    // try and stop me

    f[6]  = 0;
    f[3]  = 1;
    f[15] = 2;
    f[13] = 3;
    f[1]  = 4;
    //f[0]  = 5;

    int x = 0;
    int y = 0;
    for (int i=5; i<30000000; i++) {

        if (f[x] == -1) {
            //printf("x= %d f[x]=%d\n", x,f[x]);
            f[x] = i;
            x = 0;
            //printf("x= %d f[x]=%d\n", x,f[x]);
        } else {
            //printf("i = %d x = %d dist = %d - %d\n", i, x, i, f[x]);
            int xx = i-f[x];
            f[x] = i;
            x = xx;
        }
        

        if (i == idx-2) {
            break;
        }
    }

    printf("%d", x);

    return 0;

}

