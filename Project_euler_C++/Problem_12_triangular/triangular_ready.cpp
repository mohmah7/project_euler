#include <iostream>
#include <vector>
using namespace std;

int main() {
  int i = 0;
  int new_number =0;
  int division_number = 0;
  int new_remainder_division = 0;
  int length_of_division_list = 0;
  std::vector<int> v = { };
  std::vector<int> triangular_list ={};
  std::vector<int> division_list ={};
  while (length_of_division_list < 10) {
    //cout << i << "\n";
    //cout << "*\n";
    v.push_back(i);
    //for (int n:v){
    //	cout << n;
    //}
    
    for (int n :v){
    	new_number += n;
    }
    triangular_list.push_back(new_number); 
    division_number = new_number ;
    while (division_number > 0){
    	new_remainder_division = new_number % division_number;
        if (new_remainder_division == 0){
        	division_list.push_back(division_number);
            
        }
        division_number -=1;
    
    }
    //for (int n :triangular_list){
    //	cout << n << '\n';
    //}
   	//cout << division_list.size() << "\n";
    length_of_division_list = division_list.size();
    cout << "number is :" <<new_number << "\n";
    cout << "number of divisions is :" <<length_of_division_list << "\n";
    division_list ={};
    new_number = 0;
    i++;
  }
  return 0;
}