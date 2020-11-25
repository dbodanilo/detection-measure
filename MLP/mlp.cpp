#include <iostream>
#include <cstdlib>
#include <vector>
#include <time.h>
#include <list>

using namespace std;

class Flower
{
public:
    vector<vector<double>> data;
    vector<string> label_string;
    vector<vector<double>> label_output;

    //transforma as labels em código binário para cada classe
    void fillOutputLabel()
    {
        for (int i = 0; i < this->label_string.size(); i++)
        {
            if (this->label_string[i] == "Iris-setosa")
            {
                this->label_output.push_back({1, 0, 0});
            }
            else if (this->label_string[i] == "Iris-versicolor")
            {
                this->label_output.push_back({0, 1, 0});
            }
            else if (this->label_string[i] == "Iris-virginica")
            {
                this->label_output.push_back({0, 0, 1});
            }
        }
    }
};

class ANN
{
public:
    int input;
    int hidden;
    int processors;
    int output;
    double n;
    vector<list<int>> graph;
    vector<vector<double>> weights;

    ANN(int input, int hidden, int processors, int output, double n)
    {
        this->input = input;
        this->hidden = hidden;
        this->processors = processors;
        this->output = output;
        this->n = n;
        vector<list<int>> aux(input + output + (hidden * processors));
        vector<double> v1(input + output + (hidden * processors));
        vector<vector<double>> ax(input + output + (hidden * processors), v1);
        this->weights = ax;
        this->graph = aux;
    }
    void buildANN()
    {
        int cont = 0;
        srand(time(NULL));
        //adicionando primeiro as entradas
        for (int i = 0; i < this->input; i++)
        {

            for (int j = this->input; j < this->input + this->processors; j++)
            {
                this->graph[i].push_back(j);
                this->weights[i][j] = (rand() % 100 + 1) / 1000.0;
            }
        }
        //adicionando ao grapo o restante dos nós
        for (int i = this->input; i < this->graph.size() - this->output; i++)
        {
            if ((i - this->input) % this->processors == 0)
                cont = 0;

            for (int j = i + this->processors - cont; j < i + this->processors - cont + this->processors; j++)
            {
                if (j < this->graph.size())
                {
                    this->graph[i].push_back(j);
                    this->weights[i][j] = (rand() % 100 + 1) / 1000.0;
                }
            }
            cont++;
        }
    }

    void showNetworkConnections()
    {

        list<int>::iterator it;

        for (int i = 0; i < this->graph.size(); i++)
        {
            cout << i << " estah conectado a: ";
            for (it = this->graph[i].begin(); it != this->graph[i].end(); it++)
            {
                cout << *it << " ";
            }
            cout << endl;
        }

        for (int i = 0; i < this->weights.size(); i++)
        {
            for (int j = 0; j < this->weights[i].size(); j++)
            {
                cout << weights[i][j] << " ";
            }
            cout << endl;
        }
    }
};

class Solver
{
public:
    vector<double> fnet;
    vector<double> output;

    Solver(int tam)
    {
        vector<double> v1(tam, 0);
        vector<double> v2(tam, 0);
        this->fnet = v1;
        this->output = v2;
    }

    void solveAll(ANN g,Flower dt){

    }

};