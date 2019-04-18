MAIN=main.cpp
FLAGS=-std=c++11 -pthread
SRC_DIR=src
SRC=$(wildcard $(SRC_DIR)/*.cpp)
INCLUDE=include
LIB_DIR=lib
LIB=$(wildcard $(LIB_DIR)/*.a)
test:
	g++ $(FLAGS) $(MAIN) -I$(INCLUDE) $(SRC) -L$(LIB_DIR) $(LIB) -o output


