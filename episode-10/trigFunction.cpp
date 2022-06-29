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

double trig (Stack stack)
{
    MeshPoint &mp = *MeshPointStack(stack); //the struct to get x, y, normal, value
    double x = mp.P.x; // get the current x value
    double y = mp.P.y; // get the current y value
    return sin(x)*cos(y);
}

template<class R>
class OneOperator0s : public OneOperator {
    class E_F0_F : public E_F0mps {
      public:
        typedef R (*func)(Stack stack);
        func f;
        E_F0_F(func ff) : f(ff) {}

        AnyType operator()(Stack stack) const { return SetAny<R>(f(stack)); }
    };

    typedef R (*func)(Stack);
    func f;

    public:
        E_F0 *code(const basicAC_F0 &) const { return new E_F0_F(f); }
        OneOperator0s(func ff) : OneOperator(map_type[typeid(R).name()]),f(ff){}
};

void init()
{
  cout << "Initializing ..." << endl;
  Global.Add("trig", "(", new OneOperator0s<double>(trig));
}
LOADFUNC(init);
