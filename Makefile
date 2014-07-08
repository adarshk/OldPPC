pixel.so: clean wrapper.o
	gcc -shared -o paperpixel.so -I/usr/include/dc1394 -I/usr/include/opencv -I/usr/include/opencv -I/usr/include/boost -I/usr/include/python2.7 wrapper.o loadimage.o contours.o components.o edges.o -L/usr/local/lib -lpython2.7 -lboost_python -lpcre -lpng -ljpeg -lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_gpu -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_objdetect -lopencv_ocl -lopencv_photo -lopencv_stitching -lopencv_superres -lopencv_ts -lopencv_video -lopencv_videostab -ltiff -llzma -lidn -ldc1394


loadimage.o:
	gcc -I/usr/include/opencv -I/usr/include/opencv2 -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/load_image.cpp -o loadimage.o

edges.o: loadimage.o
	gcc -I/usr/include/opencv -I/usr/include/opencv2 -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/find_edges.cpp -o edges.o

contours.o: edges.o
	gcc -I/usr/include/opencv -I/usr/include/opencv2 -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/detect_contours.cpp -o contours.o

components.o: contours.o
	gcc -I/usr/include/opencv  -I/usr/include/opencv2 -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/find_components.cpp -o components.o

wrapper.o: components.o
	gcc -I/usr/include/opencv  -I/usr/include/opencv2 -I/usr/include/boost -I/usr/include/python2.7 -IPaperPixelCode -I/usr/local/include -c -fPIC PaperPixelCode/components_wrapper.cpp -o wrapper.o

clean:
	rm -rf contours.o components.o edges.o loadimage.o paperpixel.so wrapper.o


