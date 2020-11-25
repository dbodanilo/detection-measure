#include <iostream>
#include <cstdlib>
#include "mlp.cpp"

using namespace std;

int main(){

    ANN net = ANN(4,2,5,3);
    net.buildANN();
    net.showNetworkConnections();

    return 0;

}