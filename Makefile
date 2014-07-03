
pixel.so: clean components.o
	gcc -shared -o pixel.so contours.o components.o -L/usr/local/lib -lpython2.7 -lboost_python -lpcre

contours.o:
	gcc -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/detect_contours.cpp -o contours.o

components.o: contours.o
	gcc -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/find_components.cpp -o components.o

clean:
	rm -rf contours.o components.o pixel.so


