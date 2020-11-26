#include <iostream>
#include <cstdlib>
#include <cmath>
#include <random>
#include <chrono>
#include <algorithm>
#include "readFile.cpp"
#include "mlp.cpp"

using namespace std;

int main()
{

    string file_data = "iris-data-3-class.txt";
    string file_label = "iris-data-3-class-label.txt";

    unsigned seed = chrono::system_clock::now().time_since_epoch().count();

    Flower container = Flower();

    //aqui os dados são carregados
    container.data = readFile(file_data);
    container.label_string = readFileLabel(file_label);

    //transforma as labels em numeros (setosa -> 100, versicolor -> 010, virginica -> 001)
    container.fillOutputLabel();

    //embaralha os dados
    shuffle(container.data.begin(), container.data.end(), std::default_random_engine(seed));
    shuffle(container.label_output.begin(), container.label_output.end(), std::default_random_engine(seed));

    ANN net = ANN(4, 4, 4, 3, 0.03);
    net.buildANN();
    Solver s = Solver(net.graph.size());
    s.solveAll(net,container,1);
    // net.showNetworkConnections();

    return 0;
}