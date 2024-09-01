#include <iostream>
#include <string>

int main() {

    //These are global variables

    int row;
    int column;
    char token = 'x';
    bool draw = false;
    std::string Player1 ="";
    std::string Player2="";
    char space[3][3] = {{'1', '2', '3'},{'4', '5', '6'}, {'7', '8', '9'}};

    std::cout << "Enter the name of Player1: \n\n";
    std::cin >> Player1;
    
    std::cout << "Enter the name of Player2: \n\n";
    std::cin >> Player2;

    std::cout << Player1 << " is Player1 so he/she will play first. \n\n";
    std::cout << Player2 << " is Player2 so he/she will start second. \n\n";


    // Main code here
    std::cout << "Welcome to tic-tac-toe! To make a move, type in the number corresponding to the place on the grid below\n";

    std::cout << "     |     |   \n";
    std::cout << "  7  |  8  |  9\n";
    std::cout << "_____|_____|_____\n";
    std::cout << "     |     |    \n";
    std::cout << "  4  |  5  |  6\n";
    std::cout << "_____|_____|_____\n";
    std::cout << "     |     |   \n";
    std::cout << "  1  |  2  |  3\n";
    std::cout << "     |     |   \n";
 
    while(!functionThree()){  // so here we declare your function, it could be under function one.
        functionOne();
        functionTwo();
        functionThree();
    }

    if(token=='x' && draw == false){
        std::cout << Player1 <<" Wins!!" << std::endl;

    }

    else if(token=='o' && draw == false){
        std::cout << Player2 << " Wins!!" << std::endl;

    }

    else{
        std::cout  << "It is a Tie!!" << std::endl;
    }

    return 0;

}
