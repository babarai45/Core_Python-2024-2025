//  method overloading in C++ 
#include <iostream>
using namespace std;

class Add {
    public:
        int sum(int a, int b) {
            return a + b;
        }
        int sum(int a, int b, int c) {
            return a + b + c;
        }
};

int main() {
    Add obj;
    cout << "Sum of two numbers: " << obj.sum(10, 20) << endl;
    cout << "Sum of three numbers: " << obj.sum(10, 20, 30) << endl;
    return 0;
}

// Output

// Sum of two numbers: 30
// Sum of three numbers: 60


//  now diffrent type of parameter 
#include <iostream>

using namespace std;

class Add {
    public:
        int sum(int a, int b) {
            return a + b;
        }
        int sum(int a, int b, int c) {
            return a + b + c;
        }
        float sum(float a, float b) {
            return a + b;
        }
};

int main() {
    Add obj;
    cout << "Sum of two numbers: " << obj.sum(10, 20) << endl;
    cout << "Sum of three numbers: " << obj.sum(10, 20, 30) << endl;
    cout << "Sum of two float numbers: " << obj.sum(10.5f, 20.5f) << endl;
    return 0;
}


// Output

// Sum of two numbers: 30
// Sum of three numbers: 60

// Sum of two float numbers: 31




//  now diffrent sequence of paramete