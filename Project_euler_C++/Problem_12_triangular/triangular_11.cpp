#include <iostream>
using namespace std;

int main() {
  int i = 0;
  std::vector<int> v = { 7, 5, 16, 8 };
  while (i < 5) {
    cout << i << "\n";
    i++;
  }
  return 0;
}



//--------------------------------------------------------------------------

#include <iostream>
#include <vector>
using namespace std;

int main() {
  int i = 0;
  std::vector<int> v = { };
  while (i < 5) {
    cout << i << "\n";
    cout << "*\n";
    v.push_back(i);
    for (int n:v){
      cout << n;
    }
    i++;
  }
  return 0;
}


//---------------------------------------------------------------------------


#include <iostream>
#include <vector>
using namespace std;

int main() {
  int i = 0;
  int new_number =0;
  std::vector<int> v = { };
  std::vector<int> triangular_list ={};
  while (i < 5) {
    cout << i << "\n";
    cout << "*\n";
    v.push_back(i);
    for (int n:v){
      cout << n;
    }
    
    for (int n :v){
      new_number += n;
    }
    triangular_list.push_back(new_number);   
    new_number = 0;
    i++;
  }
  return 0;
}

//------------------------------------------------------------------------

#include <iostream>
#include <vector>
using namespace std;

int main() {
  int i = 0;
  int new_number =0;
  std::vector<int> v = { };
  std::vector<int> triangular_list ={};
  while (i < 10) {
    //cout << i << "\n";
    //cout << "*\n";
    v.push_back(i);
    //for (int n:v){
    //  cout << n;
    //}
    
    for (int n :v){
      new_number += n;
    }
    triangular_list.push_back(new_number);   
    for (int n :triangular_list){
      cout << n << '\n';
    }
    new_number = 0;
    i++;
  }
  return 0;
}

