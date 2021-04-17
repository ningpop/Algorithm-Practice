#include <string>
#include <vector>

using namespace std;

class Month{
    int date;
    
public:
    Month():date{0}{}
    Month(int d):date{d}{}
    int getDate(){
        return date;
    }
};

string solution(int a, int b) {
    string answer = "";
    Month month[12]={
        Month(31), Month(29), Month(31), Month(30), Month(31), Month(30),
        Month(31), Month(31), Month(30), Month(31), Month(30), Month(31)
    };
    int day=0;
    
    for(int i=0;i<a-1;i++){
        day += month[i].getDate();
    }
    day+=b;
    
    switch(day%7){
        case 1:
            answer="FRI";
            break;
        case 2:
            answer="SAT";
            break;
        case 3:
            answer="SUN";
            break;
        case 4:
            answer="MON";
            break;
        case 5:
            answer="TUE";
            break;
        case 6:
            answer="WED";
            break;
        default:
            answer="THU";
            break;
    }
    
    return answer;
}