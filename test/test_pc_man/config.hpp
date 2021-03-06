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


#ifndef CPPDEVTK_TEST_PC_MAN_CONFIG_HPP_INCLUDED_
#define CPPDEVTK_TEST_PC_MAN_CONFIG_HPP_INCLUDED_


#include <cppdevtk/gui/config.hpp>

#if (!(CPPDEVTK_HAVE_POWER_NOTIFIER && CPPDEVTK_HAVE_SCREENSAVER && CPPDEVTK_HAVE_SESSION && CPPDEVTK_HAVE_SESSION_MANAGER	\
		&& CPPDEVTK_HAVE_STORAGE_DEVICE_NOTIFIER))
#	error "This file requires PowerNotifier, ScreenSaver, Session, SessionManager and StorageDeviceNotifier!!!"
#endif

#if (!CPPDEVTK_PLATFORM_DESKTOP)
#	error "This project is deskyop only!!!"
#endif


#include "info.hpp"


#endif	// CPPDEVTK_TEST_PC_MAN_CONFIG_HPP_INCLUDED_
