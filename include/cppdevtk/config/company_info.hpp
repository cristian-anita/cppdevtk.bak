/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// \file
///
/// \copyright Copyright (C) 2015 - 2017 CoSoSys Ltd <info@cososys.com>\n
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


#ifdef APSTUDIO_INVOKED
#	error "This file is not editable by Microsoft Visual C++!!!"
#endif


#ifndef CPPDEVTK_CONFIG_COMPANY_INFO_HPP_INCLUDED_
#define CPPDEVTK_CONFIG_COMPANY_INFO_HPP_INCLUDED_


#include "features.hpp"


/// \defgroup config_info_company_info Company Info
/// \ingroup config_info
/// @{

#define CPPDEVTK_COMPANY_SHORT_NAME "CoSoSys"
#define CPPDEVTK_COMPANY_SHORT_NAME_SANITIZED QString(CPPDEVTK_COMPANY_SHORT_NAME).toLower().replace(' ', '_')
#define CPPDEVTK_COMPANY_LONG_NAME "CoSoSys Ltd."
#define CPPDEVTK_COMPANY_LONG_NAME_SANITIZED QString(CPPDEVTK_COMPANY_LONG_NAME).toLower().replace(' ', '_')
#define CPPDEVTK_COMPANY_COPYRIGHT "Copyright (C) 2015 - 2017 " CPPDEVTK_COMPANY_LONG_NAME ". All rights reserved. " CPPDEVTK_COMPANY_EMAIL "."
#define CPPDEVTK_COMPANY_TRADEMARKS "TM " CPPDEVTK_COMPANY_LONG_NAME "."
#define CPPDEVTK_COMPANY_HOMEPAGE "http://www.cososys.com"
#define CPPDEVTK_COMPANY_EMAIL "info@cososys.com"

/// @}	// config_info_company_info


#endif	// CPPDEVTK_CONFIG_COMPANY_INFO_HPP_INCLUDED_
