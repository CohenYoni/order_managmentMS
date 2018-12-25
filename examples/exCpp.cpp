#include <iostream>
using namespace std;

int main(int argc, char *argv[]) 
{
	if (argc == 2) {
		cout << argv[1];
		return 0;
	}
	else {
		cout << "Error Argument";
		return 1;
	}
}

//CL <name> from Dev CMD vs 2017