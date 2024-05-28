
#include <opencv2/opencv.hpp>
#include <iostream>

int main(){
	
	cv::VideoCapture cap(-1);
	cv::Mat frame;
	cv::namedWindow("yaho", cv::WINDOW_AUTOSIZE);

	if (cap.isOpened()){
		while(1){
			cap >> frame;
			cv::imshow("yaho", frame);
			if(cv::waitKey(1) == 27) break;
		}
	}

	else{
		std::cout << "No Frame" << std::endl;	
	}
	
	cv::destroyAllWindows();
	return 0;
}