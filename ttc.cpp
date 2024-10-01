#include "functions.hpp"

int main(){


    std::cout << "Enter the name of the First Player here: ";
    std::getline(std::cin, P1);                                  // This will get the input of the name of the First Player.

    std::cout << "Enter the name of the Second Player here: ";
    std::getline(std::cin, P2);                                 // This will get the input of the name of the Second player.

    std::cout << P1 << " is Player1 so he/she will play first \n";        //This will output the following responses after Player enters his/her name.
    std::cout << P2 << " is Player2 so he/she will play second \n";


    while(!functionThree()){

        functionOne();
        functionTwo();
        functionThree();

    }

 if (draw) {
        std::cout << " IT IS A DRAW." << std::endl;
    } else if (token == 'x') {
        std::cout << P2 << " WINS!!!" << std::endl;
    } else {
        std::cout << P1 << " WINS!!!" << std::endl;
    }

    return 0;
}
