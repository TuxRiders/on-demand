#include <iostream>
#include <cfloat>
#include "error.hpp"
#include "AFunction.hpp"
#include "rgraph.hpp"
#include "RNM.hpp"
#include "fem.hpp"
#include "FESpace.hpp"
#include "MeshPoint.hpp"

using namespace std;
using namespace Fem2D;

double check(Stack s, const double &a)
{
   return a;
}

double print(string *s)
{
  cout << *s << endl;
  return 0.;
}

void init()
{
  cout << "Initializing ..." << endl;
  Global.Add("check", "(", new OneOperator1s_<double, double>(check));
  Global.Add("print", "(", new OneOperator1<double, string *>(print));
}
LOADFUNC(init);
