import subprocess

result = subprocess.run(['pip', 'list'], capture_output=True, check=True, text=True)

print(result.stdout)

def Cgen():
    initial = '''#include <stdio.h>

                int main() {
                return 0;
                }'''
    with open('Cfile.c', 'w') as f:
        f.write(initial)

