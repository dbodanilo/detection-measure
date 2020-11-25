#include <iostream>
#include <cstdlib>
#include <vector>
#include <list>

using namespace std;

class ANN
{
public:
    int input;
    int hidden;
    int processors;
    int output;
    vector<list<int>> graph;

    ANN(int input, int hidden, int processors, int output)
    {
        this->input = input;
        this->hidden = hidden;
        this->processors = processors;
        this->output = output;
        vector<list<int>> aux(input + output + (hidden * processors));
        this->graph = aux;
    }
    void buildANN()
    {
        int cont = 0;
        //adicionando primeiro as entradas
        for (int i = 0; i < this->input; i++)
        {

            for (int j = this->input; j < this->input + this->processors; j++)
            {
                this->graph[i].push_back(j);
            }
        }
        //adicionando ao grapo o restante dos nós
        for (int i = this->input; i < this->graph.size()-this->output; i++)
        {
            if ((i-this->input) % this->processors == 0)
                cont = 0;

            for (int j = i + this->processors- cont; j < i + this->processors - cont+this->processors; j++)
            {
                if(j<this->graph.size())
                    this->graph[i].push_back(j);
            }
            cont++;
        }
    }

    void showNetworkConnections()
    {

        list<int>::iterator it;

        for (int i = 0; i < this->graph.size(); i++)
        {
            cout<<i<<" estah conectado a: ";
            for (it = this->graph[i].begin(); it != this->graph[i].end(); it++)
            {
                cout<<*it<<" ";
            }
            cout<<endl;
        }
    }
};