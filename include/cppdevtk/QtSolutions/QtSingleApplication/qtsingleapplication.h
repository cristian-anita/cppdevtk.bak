/****************************************************************************
**
** Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt Solutions component.
**
** $QT_BEGIN_LICENSE:BSD$
** You may use this file under the terms of the BSD license as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of Digia Plc and its Subsidiary(-ies) nor the names
**     of its contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/


#ifndef CPPDEVTK_QTSOLUTIONS_QTSINGLEAPPLICATION_QTSINGLEAPPLICATION_H_INCLUDED_
#define CPPDEVTK_QTSOLUTIONS_QTSINGLEAPPLICATION_QTSINGLEAPPLICATION_H_INCLUDED_


#include "config.hpp"
#include <cppdevtk/base/unused.hpp>

#include <QtCore/QtGlobal>
#if (QT_VERSION >= QT_VERSION_CHECK(5, 0, 0))
#include <QtWidgets/QApplication>
#else
#include <QtGui/QApplication>
#endif


namespace cppdevtk {
namespace qtsol {


class QtLocalPeer;


class CPPDEVTK_QTSINGLEAPP_EXPORT QtSingleApplication : public QApplication
{
    Q_OBJECT

public:
    QtSingleApplication(int &argc, char **argv, bool GUIenabled = true);
    QtSingleApplication(const QString &id, int &argc, char **argv);
#	if (QT_VERSION < QT_VERSION_CHECK(5, 0, 0))
    QtSingleApplication(int &argc, char **argv, Type type);
#  if defined(Q_WS_X11)
    QtSingleApplication(Display* dpy, Qt::HANDLE visual = 0, Qt::HANDLE colormap = 0);
    QtSingleApplication(Display *dpy, int &argc, char **argv, Qt::HANDLE visual = 0, Qt::HANDLE cmap= 0);
    QtSingleApplication(Display* dpy, const QString &appId, int argc, char **argv, Qt::HANDLE visual = 0, Qt::HANDLE colormap = 0);
#  endif // Q_WS_X11
#endif // QT_VERSION < 0x050000

    bool isRunning();
    QString id() const;
	
	bool unlock();

    void setActivationWindow(QWidget* aw, bool activateOnMessage = true);
    QWidget* activationWindow() const;

    // Obsolete:
    void initialize(bool dummy = true)
        { isRunning(); ::cppdevtk::base::SuppressUnusedWarning(dummy); }

public Q_SLOTS:
    bool sendMessage(const QString &message, int timeout = 5000);
    void activateWindow();


Q_SIGNALS:
    void messageReceived(const QString &message);


private:
    void sysInit(const QString &appId = QString());
    QtLocalPeer *peer;
    QWidget *actWin;
};


}	// namespace qtsol
}	// namespace cppdevtk


#endif	// CPPDEVTK_QTSOLUTIONS_QTSINGLEAPPLICATION_QTSINGLEAPPLICATION_H_INCLUDED_
