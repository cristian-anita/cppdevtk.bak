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


#ifndef CPPDEVTK_UTIL_CORE_APPLICATION_HPP_INCLUDED_
#define CPPDEVTK_UTIL_CORE_APPLICATION_HPP_INCLUDED_


#include "config.hpp"
#include "core_application_base.hpp"

#include <QtCore/QCoreApplication>


namespace cppdevtk {
namespace util {


class CPPDEVTK_UTIL_API CoreApplication: public QCoreApplication, public CoreApplicationBase {
	friend class CoreApplicationBase;
	
	Q_OBJECT
public:	
	CoreApplication(int& argc, char** argv);
	virtual ~CoreApplication();
public Q_SLOTS:
	/// \note We can not use ::cppdevtk::util::CoreApplicationBase::NotifyThrowAction here because enum must
	/// be registered to meta-object system and CoreApplicationBase does not inherit QObject, so we use int.
	void SetNotifyThrowAction(int notifyThrowAction);
private:
	Q_DISABLE_COPY(CoreApplication)
	
	// private to prevent overriding in derived classes.
	virtual bool notify(QObject* pReceiver, QEvent* pEvent);
};




/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inline functions

inline bool CoreApplication::notify(QObject* pReceiver, QEvent* pEvent) {
	return CoreApplicationBase::notify(pReceiver, pEvent);
}


}	// namespace util
}	// namespace cppdevtk


#endif	// CPPDEVTK_UTIL_CORE_APPLICATION_HPP_INCLUDED_
