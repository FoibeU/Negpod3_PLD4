#!/usr/bin/pythn3
def beginner():
    import random
    from string import ascii_lowercase
    import colorama
    from colorama import Fore
    print(Fore.YELLOW + 'You will get the following subjects')
    print("Introductions to CSS")
    print("HTML Introduction")
    print("RWD Introductioni")
def intermedium():
    import colorama
    from colorama import Fore
    print(Fore.YELLOW + 'You will get the following subjects')
    print("introduction to C")
    print("Algorithm")

def advanced():
    import colorama
    from colorama import Fore
    print( Fore.YELLOW + 'You will get the following subjects6')
    print("Python introduction")
    print("Java Introduction")
    print("Sql Introduction")

def main():
    print("Welcome to The basics in Technology Learning Platform")
    print("Select one of the following level  in which you want to start with")
    while(True):
        print("1.Beginner Level ")
        print("2. Mediam Level")
        print("3. Advanced Level")
        print("10. Exit")
        print("Enter the choice number from above")
        choice = int(input())
        if choice == 1:
            print("You have chosen Beginner Level.");
            beginner();
            print("Are you sure you want to start as  a beginner ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("\033[2;37;40m Wonderful, Now you can start learning the basics of web design\033[0;37;40m  \n" );
                print("\033[2;37;40m Cascading Style Sheets (CSS) is a stylesheet language used to\n describe the presentation of a document written in HTML or XML \n(including XML dialects such as SVG, MathML or XHTML). CSS describes how elements should be rendered on screen,\n on paper, in speech, or on other media. ")
            if ch == "A":
                html = " \033[2;37m HTML: \n is a markup language that defines the structure of your content.\n HTML consists of a series of elements, which you use to enclose,\n or wrap, different parts of the content to make it appear a certain way\n, or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else,\n can italicize words, can make the font bigger or smaller\n, and so on.Example : <!DOCTYPE html>\n<html>\n<body\n\n><h1>My First Heading</h1><p>My first paragraph.</p>\n\n</body>\n</html> "
                print(html)
                print("C. No, I'm not sure")
                break

        elif choice == 2:
            print("You have chosen a mediam level.");
            intermedium();
            print("Are you sure you want to start on intermediam level ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                    print("Wonderful, Now you can start learn the concepts of programming language and how to use algorithm");
                    print(" C is a general-purpose programming\n language created by Dennis Ritchie at the Bell Laboratories in 1972.\n Example:\n #include <stdio.h>int main() {\nint number1")
                    break
        elif choice == 3:
            print("You have chosen an advanced")
            advanced();
            print("Are you sure you want to start as an advanced ? A or B.")
            print("A. Yes, I'm sure")
            print("B. No, I'm not sure")
            ch = input()[0]
            if ch == 'A':
                print("Wonderful, Now you can start leaen how to build simple program");
                print("\033[1;37;40m  Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.It is used for:\n1. web development \n2.software development\n3. mathematics\n4.system scripting\nWhy Python?\n.Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc)\n.Python can be treated in a procedural way, an object-oriented way or a functional way.\n example :\n a = 5+5\n print(a) \noutpur: 10 , you can try it on your terminal and by keep Exercising you will learn more \033[1;37;40m \n")
                break

        elif choice == 10:
            break
        else:
            print("You have entered an invalid choice.")
if __name__ == '__main__':
    main()

