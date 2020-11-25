#include <iostream>
#include <cstdlib>
#include "mlp.cpp"

using namespace std;

int main(){

    ANN net = ANN(4,4,4,3);
    net.buildANN();
    net.showNetworkConnections();

    return 0;

}