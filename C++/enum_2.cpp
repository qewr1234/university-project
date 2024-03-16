#include <iostream>

using namespace std;

/*
enum TextAttribute{
    Bold = 1, Underline = 2, Italic = 4, Strikethrough = 8
};
*/

enum class Color{
    Red, Green, Blue
};

int main(){
    /*int textAttrs = 0;
    textAttrs |= TextAttribute :: Bold;  범위지정 연산자
    textAttrs |= TextAttribute :: Underline;

    cout << textAttrs << endl;
    if(textAttrs & Italic)
        cout << "Italic" << endl; */
    Color color = (Color)1;
    if(color == Color::Red)
        cout << "RED" << endl;
    if(color == Color::Green)
        cout << "GREEN" << endl;
    if(color == Color::Blue)
        cout << "BLUE" << endl;
}