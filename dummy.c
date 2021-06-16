#include <stdio.h>

void printIntVal(int *ptr, int len) {
	for(int i=0; i < len; i++)
		printf("%d",ptr[i]);
}

void printCharVal(char *ptr, int len) {
	for(int i=0; i < len; i++)
		printf("%c",ptr[i]);
}

int main() {
	char data[] = "SHUBHAM";
	int array[1] = {1};

	printCharVal(data, sizeof(data));
	printIntVal(array, (sizeof(array)/sizeof(int)));
	return 1;
}
