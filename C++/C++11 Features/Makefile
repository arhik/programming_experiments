CXX = g++
CXXFLAGS += -std=c++14 -Wall
# ifeq ($(BUILD), debug)
# CXXFLAGS += -O0 -g
# else
# CXXFLAGS += -O2 -s -DNDEBUG

# endif
CXXFLAGS += -O0 -g
autotest: ASSERT.o
	${CXX} ${CXXFLAGS} autotest.cpp -o prog