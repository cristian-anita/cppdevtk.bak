/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// \file
///
/// \copyright Copyright (C) 2015 - 2018 CoSoSys Ltd <info@cososys.com>\n
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


#include "config.hpp"
#include "init_resources.hpp"
#include "widget.hpp"
#include <cppdevtk/gui/application.hpp>
#include <cppdevtk/gui/message_box.hpp>
#include <cppdevtk/base/logger.hpp>
#include <cppdevtk/base/qiostream.hpp>
#include <cppdevtk/base/exception.hpp>
#include <cppdevtk/base/cassert.hpp>
#include <cppdevtk/base/info_tr.hpp>

#include <QtCore/QString>
#ifndef CPPDEVTK_SHARED
#	include <QtCore/QtPlugin>
#endif
#include <QtGui/QIcon>

#include <cstdlib>


#ifndef CPPDEVTK_SHARED
#if (QT_VERSION >= QT_VERSION_CHECK(5, 0, 0))
Q_IMPORT_PLUGIN(QICOPlugin)
#else
Q_IMPORT_PLUGIN(qico)
#endif
#endif


using ::cppdevtk::gui::Application;
using ::cppdevtk::gui::MessageBox;
using ::cppdevtk::base::qcerr;
using ::cppdevtk::base::Exception;
using ::std::exception;


int main(int argc, char* argv[]) try {
	::cppdevtk::test_caps_lock_widget::InitResources();
	
	CPPDEVTK_ASSERT(Application::quitOnLastWindowClosed());
	
	Application::SetInfo(CPPDEVTK_COMPANY_SHORT_NAME_SANITIZED, CPPDEVTK_COMPANY_HOMEPAGE,
			CPPDEVTK_SHORT_NAME_SANITIZED, CPPDEVTK_VERSION_STRING);
	Application::SetQmInfo(":/cppdevtk/test_caps_lock_widget/res/tr", "tr_");
	
	Application application(argc, argv);
	application.SetPreferSystemLocale(true);
	application.SetCurrentLanguageInfo(application.GetCurrentLanguageInfo());
	
	Application::setWindowIcon(QIcon(":/cppdevtk/test_caps_lock_widget/res/ico/application.ico"));
	
	try {
		::cppdevtk::test_caps_lock_widget::Widget widget;
		widget.show();
		
		return application.exec();
	}
	catch (const exception& exc) {
		CPPDEVTK_LOG_ERROR("caught ::std::exception: " << Exception::GetDetailedInfo(exc));
		MessageBox::Critical(application.GetDefaultWindow(),
				Application::translate(CPPDEVTK_INFO_TR_CTX, CPPDEVTK_LONG_NAME_TR),
				Application::translate("main", "Caught exception: %1").arg(exc.what()), exc);
		
		return EXIT_FAILURE;
	}
	catch (...) {
		CPPDEVTK_LOG_ERROR("caught unknown exception!");
		MessageBox::Critical(application.GetDefaultWindow(),
				Application::translate(CPPDEVTK_INFO_TR_CTX, CPPDEVTK_LONG_NAME_TR),
				Application::translate("main", "Caught unknown exception!"));
		
		return EXIT_FAILURE;
	}
}
catch (const exception& exc) {
	const QString kErrMsg = QString("caught ::std::exception: %1\nDetails: %2").arg(
			exc.what(), Exception::GetDetailedInfo(exc));
	CPPDEVTK_LOG_FATAL(kErrMsg);
	qcerr << "Fatal Error: " << kErrMsg << endl;
	
	return EXIT_FAILURE;
}
catch (...) {
	const QString kErrMsg("caught unknown exception!!!");
	CPPDEVTK_LOG_FATAL(kErrMsg);
	qcerr << "Fatal Error: " << kErrMsg << endl;
	
	return EXIT_FAILURE;
}
