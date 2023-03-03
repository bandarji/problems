#include <stdio.h>
#include <pwd.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    struct passwd *u;
    int ruid = getuid();
    int euid = geteuid();

    u = getpwuid(ruid);
    if (u) {
        printf("Name: %s\n", u->pw_name);
    }

    printf("UID Real, Effective: %d, %d\n", ruid, euid);

    return 0;
}