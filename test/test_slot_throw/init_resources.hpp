/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// \file
///
/// \copyright Copyright (C) 2015 - 2020 CoSoSys Ltd <info@cososys.com>\n
/// Licensed under the Apache License, Version 2.0 (the "License");\n
/// you may not use this file except in compliance with the License.\n
/// You may obtain a copy of the License at\n
/// http://www.apache.org/licenses/LICENSE-2.0\n
/// Unless required by applicable law or agreed to in writing, software\n
/// distributed under the License is distributed on an "AS IS" BASIS,\n
/// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n
/// See the License for the specific language governing permissions and\n
/// limitations under the License.\n
/// Please see the file COPYING.
///
/// \authors Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#ifndef CPPDEVTK_TEST_SLOT_THROW_INIT_RESOURCES_HPP_INCLUDED_
#define CPPDEVTK_TEST_SLOT_THROW_INIT_RESOURCES_HPP_INCLUDED_


#include "config.hpp"
#include <cppdevtk/base/init_resources.hpp>
#include <cppdevtk/util/init_resources.hpp>
#if (CPPDEVTK_ENABLE_QT_SOLUTIONS)
#include <cppdevtk/QtSolutions/QtCopyDialog/init_resources.hpp>
#endif
#include <cppdevtk/gui/init_resources.hpp>

#include <QtCore/QDir>


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Initialize resources for cppdevtk/test_slot_throw subproject.
/// \remark Not in namespace.
void CppDevTkTestSlotThrowInitResources();


namespace cppdevtk {
namespace test_slot_throw {


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Initialize all resources for cppdevtk/test_slot_throw subproject.
void InitResources();


}	// namespace test_slot_throw
}	// namespace cppdevtk




/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inline functions.

inline void CppDevTkTestSlotThrowInitResources() {
#	ifndef CPPDEVTK_SHARED
	Q_INIT_RESOURCE(cppdevtk_test_slot_throw);
	Q_INIT_RESOURCE(cppdevtk_test_slot_throw_customization);
#	endif
}


namespace cppdevtk {
namespace test_slot_throw {


inline void InitResources() {
	CppDevTkBaseInitResources();
	CppDevTkUtilInitResources();
#	if (CPPDEVTK_ENABLE_QT_SOLUTIONS)
	CppDevTkQtSolutionsQtCopyDialogInitResources();
#	endif
	CppDevTkGuiInitResources();
	
	CppDevTkTestSlotThrowInitResources();
}


}	// namespace test_slot_throw
}	// namespace cppdevtk


#endif	// CPPDEVTK_TEST_SLOT_THROW_INIT_RESOURCES_HPP_INCLUDED_
