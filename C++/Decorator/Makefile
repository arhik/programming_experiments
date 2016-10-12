include Makefile.config

test : ${OBJS}
	${CXX} ${OBJS} -o test 

lib: libex14(${OBJS})

libex14.${SHARED_LIBRARY_EXTENSION}: ${OBJS}
	${CXX} ${SHARED_LIBRARY_FLAG} -o  $@ $^

clean : ${OBJS} ${DEPS} test 
	rm ${OBJS} ${DEPS} test

cleanlib: libex14 libex14.so
	rm libex14 libex14.so`

etags:
	etags *.cpp *.h

help:
	-@echo "make test: make the executable"
	-@echo "make etags: build the etags file"
	-@echo "make clean: clean the build files"