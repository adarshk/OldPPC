//
//  main.cpp
//  PaperPixelCode
//
//  Created by Adarsh Kosuru on 6/30/14.
//  Copyright (c) 2014 Frog. All rights reserved.
//


#include <iostream>
#include <string>
#include <unistd.h>

#include "find_components.h"


using namespace ppc;

int main(int argc,char** argv){
    
    
    
    char * dir = getcwd(NULL, 0);
    //    printf("Current dir: %s", dir);
    string path =  string(dir) + "/Tearsheet.png";
    
    Components com(path);
    com.find();
//    com.save_image(string(dir));
    
}
