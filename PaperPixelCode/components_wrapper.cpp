//
//	components_wrapper.cpp
//	PaperPixelCode
//
//
//  Anderson Miller on 7/7/14
//  Copyright (c) 2014 Frog. All rights reserved.
//

#include "components_wrapper.h"

using namespace boost::python;

BOOST_PYTHON_MODULE(pixel){

	class_<ppc::Components>("Components",init<std::string>())
		.def("print_values",&ppc::Components::print_values);
//.def(init<std::string>()).
}
