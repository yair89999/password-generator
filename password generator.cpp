#include <iostream>
#include <bits/stdc++.h> 
#include <ctime>

using namespace std;


string sLowerCaseLetters = "abcdefghijklmnopqrstuvwxyz";
string sUpperCaseLetters = "";
string sNumbers = "123456789";
string sSigns = "!@#$%&(){}_+-/^*=.,|[]`;:<~>";

int getRandomNum(int max, int min){
    srand((unsigned) time(0)); //seed
    int range = max - min + 1;
    int num = rand() % range + min;
    return num;
}
string generatePassword(int nLength,char cWithLowercaseLetters,char cWithUppercaseLetters,char cWithNumbers,char cWithSigns){
    string sPassword = "";
    
    string sLowerLInFunc,sUpperLInFunc,sNumbersInFunc,sSignsInFunc;
    // putting everything 
    if (cWithLowercaseLetters == 'y'){
        sLowerLInFunc = sLowerCaseLetters;
    }
    if (cWithUppercaseLetters == 'y'){
        sUpperLInFunc = sUpperCaseLetters;
    }
    if (cWithNumbers == 'y'){
        sNumbersInFunc = sNumbers;
    }
    if (cWithSigns == 'y'){
        sSignsInFunc = sSigns;
    }

    string sOptionalCharacters = sLowerLInFunc+sNumbersInFunc+sSignsInFunc+sUpperLInFunc;
    for (int i =0; i < nLength; i ++){
        int index = getRandomNum(sOptionalCharacters.length(),0);
        sPassword += sOptionalCharacters[index];
        sOptionalCharacters.erase(index,index+1);
    }
    return sPassword;
}

int main(){
    // setting the upper case letters string(appending to the string)
    for (char c:sLowerCaseLetters){
        sUpperCaseLetters += char(c - 32);
    }
    // the code itself(after the setups)
    // getting the length and what is in the password input
    int nLength = -1;
    char cWithLowercaseLetters, cWithUppercaseLetters, cWithNumbers, cWithSigns;

    while (nLength <= 0){
        cout << "Enter the password length: ";
        cin >> nLength;
    }
    while (cWithLowercaseLetters != 'y' && cWithLowercaseLetters != 'n'){
        cout << "With Lowercase letters(y/n)?";
        cin >> cWithLowercaseLetters;
    }
    while (cWithUppercaseLetters != 'y' && cWithUppercaseLetters != 'n'){
        cout << "With Uppercase letters(y/n)?";
        cin >> cWithUppercaseLetters;
    }
    while (cWithNumbers != 'y' && cWithNumbers != 'n'){
        cout << "With numbers(y/n)?";
        cin >> cWithNumbers;
    }
    while (cWithSigns != 'y' && cWithSigns != 'n'){
        cout << "With signs(y/n)?";
        cin >> cWithSigns;
    }

    // calling for the function that makes the password
    string password = generatePassword(nLength, cWithLowercaseLetters,cWithUppercaseLetters,cWithNumbers,cWithSigns);
    if (password == ""){
        cout << "This code couldn't create you a password with the given parameters";
    } else {
        cout << "the generated password is:  " << password;
    }
}