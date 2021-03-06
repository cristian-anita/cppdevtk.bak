#
# spec file for package cppdevtk
#
# Copyright (C) 2015 - 2020 CoSoSys Ltd <info@cososys.com>.
#
# Licensed under the Apache License, Version 2.0.
# Please see the file COPYING.

# Please submit bugfixes or comments via https://github.com/cososys/cppdevtk/issues
#


# suse_version, sle_version, is_opensuse (note macros escaped in comments):
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto#Detect_a_distribution_flavor_for_special_code
# - Tumbleweed: suse_version 1550
#	%%if 0%%{?suse_version} >= 1550
# - Leap 15.1: suse_version 1500, sle_version 150100
#	%%if 0%%{?sle_version} == 150100 && 0%%{?is_opensuse}
# - Leap 15.0: suse_version 1500, sle_version 150000
#	%%if 0%%{?sle_version} == 150000 && 0%%{?is_opensuse}
# - Leap 42.3: suse_version 1315, sle_version 120300
#	%%if 0%%{?sle_version} == 120300 && 0%%{?is_opensuse}
# - SLE15: sle_version 150000
#	%%if 0%%{?sle_version} == 150000 && !0%%{?is_opensuse}
# - SLE12 SP3: sle_version 120300
#	%%if 0%%{?sle_version} == 120300 && !0%%{?is_opensuse}


# TODO: modify as desired
%define cososys_build 1
%define debug_build 0
%define debug_package %{nil}

# CentOS minor version
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
%define centos_minor_ver 0
%endif
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
%define centos_minor_ver 7
%endif
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
%define centos_minor_ver 10
%endif
%endif


# Non-modifyable stuff starts here


%if %{cososys_build}
%define _prefix /opt/cososys
%define _datadir /usr/share
%define _sysconfdir /etc
%endif
%ifarch x86_64 amd64
%define rpathdir %{_prefix}/lib64
%if (0%{?centos} || 0%{?rhel})
%define _jnidir %{_prefix}/lib64/java
%endif
%else
%define rpathdir %{_prefix}/lib
%endif

# Qt 4 or 5
%if (0%{?suse_version})
%define with_qt5 1
%endif
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
%define with_qt5 1
%endif
# Qt5 is available on CentOS 7 >= 7.2 (EPEL) and 7.3 (official)
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
%if (%{centos_minor_ver} >= 2)
%define with_qt5 1
%else
%define with_qt5 0
%endif
%endif
# Qt5 is available on CentOS 6 >= 6.6 (EPEL)
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
%if (%{centos_minor_ver} >= 6)
%define with_qt5 1
%else
%define with_qt5 0
%endif
%endif
%endif


# norootforbuild


Name: cppdevtk
Version: 1.1.2
%if (0%{?centos} || 0%{?rhel})
Release: 1.el%{rhel}_%{centos_minor_ver}
%else
Release: 1
%endif
Summary: C++ Development Toolkit
License: Apache License 2.0
Group: System/Libraries
Url: https://github.com/cososys/cppdevtk
Vendor: CoSoSys Ltd
Packager: Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
Source: %{name}-%{version}.tar.bz2
BuildRequires: libstdc++-devel glibc-devel
%if (%{with_qt5})
%if (0%{?suse_version})
BuildRequires: libqt5-qtbase-devel
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: qt5-qtbase-devel
%endif
%else
%if (0%{?suse_version})
BuildRequires: libqt4-devel
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: qt-devel
%endif
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
CppDevTk is a collection of libraries for C++ development.


%package -n lib%{name}-base
Summary: CppDevTk base library
Group: System/Libraries
BuildRequires: boost-devel
%if %{cososys_build}
Requires: cososys-filesystem >= 1.1.1
%endif
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-base
CppDevTk base library.


%package -n lib%{name}-qtsol-qtservice
Summary: CppDevTk QtSolutions QtService library
Group: System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-qtsol-qtservice
CppDevTk QtSolutions QtService library.


%package -n lib%{name}-qtsol-qtlockedfile
Summary: CppDevTk QtSolutions QtLockedFile library
Group: System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-qtsol-qtlockedfile
CppDevTk QtSolutions QtLockedFile library.


%package -n lib%{name}-qtsol-qtsinglecoreapplication
Summary: CppDevTk QtSolutions QtSingleCoreApplication library
Group: System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-qtsol-qtsinglecoreapplication
CppDevTk QtSolutions QtSingleCoreApplication library.


%package -n lib%{name}-util
Summary: CppDevTk util library
Group: System/Libraries
BuildRequires: zlib-devel
%if (0%{?suse_version})
BuildRequires: libudev-devel
%endif
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
BuildRequires: systemd-devel
%endif
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
BuildRequires: systemd-devel
%endif
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
BuildRequires: libudev-devel
%endif
%endif
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-util
CppDevTk util library.


%package -n lib%{name}-jni
Summary: CppDevTk jni library
Group: System/Libraries
%if (0%{?suse_version})
%if (%{?suse_version} >= 1550)
BuildRequires: java-12-openjdk-devel
%else
%if (0%{?sle_version} == 150100)
BuildRequires: java-11-openjdk-devel
%else
%if (0%{?sle_version} == 150000)
BuildRequires: java-10-openjdk-devel
%else
BuildRequires: java-1_8_0-openjdk-devel
%endif
%endif
%endif
%endif
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
BuildRequires: java-1.8.0-openjdk-devel
%endif
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
BuildRequires: java-1.8.0-openjdk-devel
%endif
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
BuildRequires: java-1.8.0-openjdk-devel
%endif
%endif
Requires: java >= 1.8.0
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-jni
CppDevTk jni library.


%package -n lib%{name}-qtsol-qtcopydialog
Summary: CppDevTk QtSolutions QtCopyDialog library
Group: System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-qtsol-qtcopydialog
CppDevTk QtSolutions QtCopyDialog library.


%package -n lib%{name}-qtsol-qtsingleapplication
Summary: CppDevTk QtSolutions QtSingleApplication library
Group: System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-qtsol-qtsingleapplication
CppDevTk QtSolutions QtSingleApplication library.


%package -n lib%{name}-gui
Summary: CppDevTk gui library
Group: System/Libraries
BuildRequires: libXScrnSaver-devel
BuildRequires: libX11-devel
%if (0%{?suse_version})
%if (%{?suse_version} >= 1550)
BuildRequires: xorgproto-devel
%else
BuildRequires: xproto-devel
%endif
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: xorg-x11-proto-devel
%endif
%if (%{with_qt5})
%if (0%{?suse_version})
BuildRequires: libqt5-qtx11extras-devel
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: qt5-qtx11extras-devel
%endif
%else
%if (0%{?centos} || 0%{?rhel})
BuildRequires: qt-x11
%endif
%endif
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description -n lib%{name}-gui
CppDevTk gui library.


%package -n lib%{name}
Summary: CppDevTk libraries
Group: System/Libraries
Requires: lib%{name}-base = %{version}
Requires: lib%{name}-qtsol-qtservice = %{version}
Requires: lib%{name}-qtsol-qtlockedfile = %{version}
Requires: lib%{name}-qtsol-qtsinglecoreapplication = %{version}
Requires: lib%{name}-util = %{version}
Requires: lib%{name}-jni = %{version}
Requires: lib%{name}-qtsol-qtcopydialog = %{version}
Requires: lib%{name}-qtsol-qtsingleapplication = %{version}
Requires: lib%{name}-gui = %{version}

%description -n lib%{name}
Convenience package to install all %{name} libraries.




%package base-devel
Summary: Development files for lib%{name}-base
Group: Development/Libraries/C and C++
Requires: libstdc++-devel glibc-devel
Requires: boost-devel
%if (%{with_qt5})
%if (0%{?suse_version})
Requires: libqt5-qtbase-devel
%endif
%if (0%{?centos} || 0%{?rhel})
Requires: qt5-qtbase-devel
%endif
%else
%if (0%{?suse_version})
Requires: libqt4-devel
%endif
%if (0%{?centos} || 0%{?rhel})
Requires: qt-devel
%endif
%endif
Requires: lib%{name}-base = %{version}

%description base-devel
This package contains libraries and header files for
developing applications that use lib%{name}-base.


%package qtsol-qtservice-devel
Summary: Development files for lib%{name}-qtsol-qtservice
Group: Development/Libraries/C and C++
Requires: lib%{name}-qtsol-qtservice = %{version}
Requires: %{name}-base-devel = %{version}

%description qtsol-qtservice-devel
This package contains libraries and header files for
developing applications that use lib%{name}-qtsol-qtservice.


%package qtsol-qtlockedfile-devel
Summary: Development files for lib%{name}-qtsol-qtlockedfile
Group: Development/Libraries/C and C++
Requires: lib%{name}-qtsol-qtlockedfile = %{version}
Requires: %{name}-base-devel = %{version}

%description qtsol-qtlockedfile-devel
This package contains libraries and header files for
developing applications that use lib%{name}-qtsol-qtlockedfile.


%package qtsol-qtsinglecoreapplication-devel
Summary: Development files for lib%{name}-qtsol-qtsinglecoreapplication
Group: Development/Libraries/C and C++
Requires: lib%{name}-qtsol-qtsinglecoreapplication = %{version}
Requires: %{name}-qtsol-qtlockedfile-devel = %{version}
Requires: %{name}-base-devel = %{version}

%description qtsol-qtsinglecoreapplication-devel
This package contains libraries and header files for
developing applications that use lib%{name}-qtsol-qtsinglecoreapplication.


%package util-devel
Summary: Development files for lib%{name}-util
Group: Development/Libraries/C and C++
%if (0%{?suse_version})
Requires: libudev-devel
%endif
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
Requires: systemd-devel
%endif
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
Requires: systemd-devel
%endif
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
Requires: libudev-devel
%endif
%endif
Requires: zlib-devel
Requires: lib%{name}-util = %{version}
Requires: %{name}-qtsol-qtservice-devel = %{version}
Requires: %{name}-qtsol-qtlockedfile-devel = %{version}
Requires: %{name}-qtsol-qtsinglecoreapplication-devel = %{version}
Requires: %{name}-base-devel = %{version}

%description util-devel
This package contains libraries and header files for
developing applications that use lib%{name}-util.


%package jni-devel
Summary: Development files for lib%{name}-jni
Group: Development/Libraries/C and C++
%if (0%{?suse_version})
%if (%{?suse_version} >= 1550)
Requires: java-12-openjdk-devel
%else
%if (0%{?sle_version} == 150100)
Requires: java-11-openjdk-devel
%else
%if (0%{?sle_version} == 150000)
Requires: java-10-openjdk-devel
%else
Requires: java-1_8_0-openjdk-devel
%endif
%endif
%endif
%endif
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} == 8 || 0%{?rhel} == 8)
Requires: java-1.8.0-openjdk-devel
%endif
%if (0%{?centos} == 7 || 0%{?rhel} == 7)
Requires: java-1.8.0-openjdk-devel
%endif
%if (0%{?centos} == 6 || 0%{?rhel} == 6)
Requires: java-1.8.0-openjdk-devel
%endif
%endif
Requires: lib%{name}-jni = %{version}
Requires: %{name}-util-devel = %{version}

%description jni-devel
This package contains libraries and header files for
developing applications that use lib%{name}-jni.


%package qtsol-qtcopydialog-devel
Summary: Development files for lib%{name}-qtsol-qtcopydialog
Group: Development/Libraries/C and C++
Requires: lib%{name}-qtsol-qtcopydialog = %{version}
Requires: %{name}-util-devel = %{version}

%description qtsol-qtcopydialog-devel
This package contains libraries and header files for
developing applications that use lib%{name}-qtsol-qtcopydialog.


%package qtsol-qtsingleapplication-devel
Summary: Development files for lib%{name}-qtsol-qtsingleapplication
Group: Development/Libraries/C and C++
Requires: lib%{name}-qtsol-qtsingleapplication = %{version}
Requires: %{name}-util-devel = %{version}

%description qtsol-qtsingleapplication-devel
This package contains libraries and header files for
developing applications that use lib%{name}-qtsol-qtsingleapplication.


%package gui-devel
Summary: Development files for lib%{name}-gui
Group: Development/Libraries/C and C++
Requires: libXScrnSaver-devel
Requires: libX11-devel
%if (0%{?suse_version})
%if (%{?suse_version} >= 1550)
Requires: xorgproto-devel
%else
Requires: xproto-devel
%endif
%endif
%if (0%{?centos} || 0%{?rhel})
Requires: xorg-x11-proto-devel
%endif
%if (%{with_qt5})
%if (0%{?suse_version})
Requires: libqt5-qtx11extras-devel
%endif
%if (0%{?centos} || 0%{?rhel})
Requires: qt5-qtx11extras-devel
%endif
%else
%if (0%{?centos} || 0%{?rhel})
Requires: qt-x11
%endif
%endif
Requires: lib%{name}-gui = %{version}
Requires: %{name}-qtsol-qtcopydialog-devel = %{version}
Requires: %{name}-qtsol-qtsingleapplication-devel = %{version}
Requires: %{name}-util-devel = %{version}

%description gui-devel
This package contains libraries and header files for
developing applications that use lib%{name}-gui.


%package devel
Summary: Development files for %{name}
Group: Development/Libraries/C and C++
Requires: %{name}-base-devel = %{version}
Requires: %{name}-qtsol-qtservice-devel = %{version}
Requires: %{name}-qtsol-qtlockedfile-devel = %{version}
Requires: %{name}-qtsol-qtsinglecoreapplication-devel = %{version}
Requires: %{name}-util-devel = %{version}
Requires: %{name}-jni-devel = %{version}
Requires: %{name}-qtsol-qtcopydialog-devel = %{version}
Requires: %{name}-qtsol-qtsingleapplication-devel = %{version}
Requires: %{name}-gui-devel = %{version}

%description devel
Convenience package to install all %{name} devel packages.




%package test-base
Summary: Test applications for lib%{name}-base
Group: Development/Libraries/C and C++
%if (0%{?suse_version})
BuildRequires: update-desktop-files
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: desktop-file-utils
%endif

%description test-base
This package contains applications for testing lib%{name}-base.


%package test-util
Summary: Test applications for lib%{name}-util
Group: Development/Libraries/C and C++
%if (0%{?suse_version})
BuildRequires: update-desktop-files
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: desktop-file-utils
%endif

%description test-util
This package contains applications for testing lib%{name}-util.


%package test-gui
Summary: Test applications for lib%{name}-gui
Group: Development/Libraries/C and C++
%if (0%{?suse_version})
BuildRequires: update-desktop-files
%endif
%if (0%{?centos} || 0%{?rhel})
BuildRequires: desktop-file-utils
%endif

%description test-gui
This package contains applications for testing lib%{name}-gui.


%package test
Summary: Test applications for %{name}
Group: Development/Libraries/C and C++
Requires: %{name}-test-base = %{version}
Requires: %{name}-test-util = %{version}
Requires: %{name}-test-gui = %{version}

%description test
Convenience package to install all %{name} test packages.




%debug_package




%prep
%setup -q


%build

%if (0%{?suse_version})
%if (!0%{?is_opensuse})
echo "SLED is not supported; only openSUSE!!!"
exit 1
%endif
%if (%{suse_version} < 1315)
echo "openSUSE < Leap 42.3 and SLED < 12SP3 are not supported!!!"
exit 1
%endif
%else
%if (0%{?centos} || 0%{?rhel})
%if (0%{?centos} < 6 || 0%{?rhel} < 6)
echo "CentOS (Red Hat) < 6 is not supported!!!"
exit 1
%endif
%else
echo "This distribution is not supported!!!"
exit 1
%endif
%endif


%if (%{with_qt5})
qmake-qt5	\
%else
%if (0%{?centos} || 0%{?rhel})
qmake-qt4	\
%endif
%if (0%{?suse_version})
qmake	\
%endif
%endif
	./cppdevtk.pro -r -spec linux-g++	\
%if %{debug_build}
	CONFIG*=debug CONFIG-=release CONFIG-=debug_and_release	\
%else
	CONFIG*=release CONFIG-=debug CONFIG-=debug_and_release	\
%endif
	CONFIG*=shared CONFIG-=static CONFIG-=static_and_shared	\
	CONFIG+=cppdevtk_rpmbuild	\
	CPPDEVTK_PREFIX=%{buildroot}/%{_prefix}	\
	CPPDEVTK_RPATHDIR=%{rpathdir}	\
	CPPDEVTK_DATA_ROOT_DIR=%{buildroot}/%{_datadir}	\
	CPPDEVTK_SYS_CONF_DIR=%{buildroot}/%{_sysconfdir}	\
	CPPDEVTK_LOCAL_STATE_DIR=%{buildroot}/%{_localstatedir}	\
	&& make qmake_all
	
#	CPPDEVTK_THIRD_PARTY_PREFIX=%{_prefix}

# make_build is not available on all distro we support
make %{_smp_mflags}


%install
%make_install


%clean
%__rm -rf %{buildroot}




%pre
case "$1" in
	1)
		# install
	;;
	2)
		# upgrade
	;;
esac
exit 0


%post
/sbin/ldconfig
case "$1" in
	1)
		# install
	;;
	2)
		# upgrade
	;;
esac
exit 0


%preun
case "$1" in
	0)
		# uninstall
	;;
	1)
		# upgrade
	;;
esac
exit 0


%postun
/sbin/ldconfig
case "$1" in
	0)
		# uninstall
	;;
	1)
		# upgrade
	;;
esac
exit 0




%files -n lib%{name}-base
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_base.so.*


%files -n lib%{name}-qtsol-qtservice
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_qtsol_qtservice.so.*


%files -n lib%{name}-qtsol-qtlockedfile
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_qtsol_qtlockedfile.so.*


%files -n lib%{name}-qtsol-qtsinglecoreapplication
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_qtsol_qtsinglecoreapplication.so.*


%files -n lib%{name}-util
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_util.so.*


%files -n lib%{name}-jni
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_jnidir}/lib%{name}-jni.so.*


%files -n lib%{name}-qtsol-qtcopydialog
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_qtsol_qtcopydialog.so.*


%files -n lib%{name}-qtsol-qtsingleapplication
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_qtsol_qtsingleapplication.so.*


%files -n lib%{name}-gui
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_libdir}/lib%{name}_gui.so.*


%files -n lib%{name}
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO



%files base-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO doc/cppdevtk_api.chm
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}/config
%dir %{_includedir}/%{name}/base
%{_includedir}/%{name}/config/*
%{_includedir}/%{name}/base/*
%{_libdir}/lib%{name}_base.so
%{_libdir}/lib%{name}_base.prl


%files qtsol-qtservice-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/QtSolutions
%dir %{_includedir}/%{name}/QtSolutions/QtService
%{_includedir}/%{name}/QtSolutions/QtService/*
%{_libdir}/lib%{name}_qtsol_qtservice.so
%{_libdir}/lib%{name}_qtsol_qtservice.prl


%files qtsol-qtlockedfile-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/QtSolutions
%dir %{_includedir}/%{name}/QtSolutions/QtLockedFile
%{_includedir}/%{name}/QtSolutions/QtLockedFile/*
%{_libdir}/lib%{name}_qtsol_qtlockedfile.so
%{_libdir}/lib%{name}_qtsol_qtlockedfile.prl


%files qtsol-qtsinglecoreapplication-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/QtSolutions
%dir %{_includedir}/%{name}/QtSolutions/QtSingleCoreApplication
%{_includedir}/%{name}/QtSolutions/QtSingleCoreApplication/*
%{_libdir}/lib%{name}_qtsol_qtsinglecoreapplication.so
%{_libdir}/lib%{name}_qtsol_qtsinglecoreapplication.prl


%files util-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/util
%{_includedir}/%{name}/util/*
%{_libdir}/lib%{name}_util.so
%{_libdir}/lib%{name}_util.prl


%files jni-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/jni
%{_includedir}/%{name}/jni/*
%{_jnidir}/lib%{name}-jni.so
%{_jnidir}/lib%{name}-jni.prl


%files qtsol-qtcopydialog-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/QtSolutions
%dir %{_includedir}/%{name}/QtSolutions/QtCopyDialog
%{_includedir}/%{name}/QtSolutions/QtCopyDialog/*
%{_libdir}/lib%{name}_qtsol_qtcopydialog.so
%{_libdir}/lib%{name}_qtsol_qtcopydialog.prl


%files qtsol-qtsingleapplication-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/QtSolutions
%dir %{_includedir}/%{name}/QtSolutions/QtSingleApplication
%{_includedir}/%{name}/QtSolutions/QtSingleApplication/*
%{_libdir}/lib%{name}_qtsol_qtsingleapplication.so
%{_libdir}/lib%{name}_qtsol_qtsingleapplication.prl


%files gui-devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%dir %{_includedir}/%{name}/gui
%{_includedir}/%{name}/gui/*
%{_libdir}/lib%{name}_gui.so
%{_libdir}/lib%{name}_gui.prl


%files devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO




%files test-base
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_bindir}/%{name}_test_base
%{_bindir}/%{name}_test_config


%files test-util
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_bindir}/%{name}_test_service
%{_bindir}/%{name}_test_term_sig
%{_bindir}/%{name}_test_util


%files test-gui
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO
%{_bindir}/%{name}_test_caps_lock_widget
%{_bindir}/%{name}_test_disk_space_widget
%{_bindir}/%{name}_test_invisible_widget
%{_bindir}/%{name}_test_localization
%{_bindir}/%{name}_test_pc_man
%{_bindir}/%{name}_test_service_controller
%{_bindir}/%{name}_test_slot_throw
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*


%files test
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING FAQ NEWS README THANKS TODO




%changelog
* Wed Nov 27 2019 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.1.2.1
- added CentOS 8
- SetStyleSheetFromFileCross(): added support for Android and iOS
- updated CentOS 7 to 7.7
* Thu Sep 10 2019 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.1.1.1
- added MimeDatabase
- added openSUSE Leap 15.1
- executor: improved cancellation
- qmake files cleanup
- added CPPDEVTK_ON_BLOCK_EXIT_CATCH
- added CPPDEVTK_NO_INLINE and CPPDEVTK_FORCE_INLINE
- removed IsMangled()
- log to file
- improved os ver checks
- large file support checks
- embed Qt translations only in static build
- openSUSE Leap 15 bug #1094735 was fixed; removed workaround
- openSUSE Tumbleweed: gcc 9.1.1 + boost 1.69.0 + Qt 5.13.0
- iOS >= 9 (default 10)
- Android >= 4.0.3 (API level 15) (default 4.4.2 (API level 19))
- updated JNI_VERSION: 1.6 on Android and Mac OS X < 10.7, 1.8 on remaining platforms
- updated Qt to 5.9.7 on Ubuntu 16.04 and 14.04
- updated Qt to 5.9.8 on Win, Mac and iOS
- updated Ubuntu to 18.04.3, 16.04.6 and 14.04.6
- updated CentOS 7 to 7.6
- updated third party libs; modified for new third party dir structure on Win and Mac
- executor: workaround for Qt bug #6799
- executor: if Qt < 5.6.2 then may be affected by Qt bug #54831
- custom wizard back()
* Mon Jul 2 2018 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.1.0.1
- added PosixSignalsWatcher (Unix)
- CoreApplicationBase: added support for termination signals (Unix + Windows)
- added GetCurrentProcessId()
- added ScreenSaver (desktops only)
- added DeviceNotifier (desktops only)
- added PowerNotifier (desktops only)
- added SessionManager + Session (desktops only)
- added ServiceBase/Service/ServiceController supporting termination signals and reload config
- added support for Ubuntu 18.04
- added support for openSUSE Leap 15 (Leap 42.2 no longer supported; EOL since 26 Jan 2018)
- removed ComputerManager (replaced by SessionManager)
- removed GetUserIdleTime() (replaced by Session::GetIdleTime())
- do not conflict with boost signals
- zlib dependency is optional (affects QZipReader and QZipWriter)
- CoreApplicationBase::SetInfo(): added componentName
- GCC/Clang visibility
- template explicit instantiation review
- separated QtSolutions libraries
- Mac OS X: QMAKE_SONAME_PREFIX = @rpath and QMAKE_RPATHDIR *= @loader_path/../Frameworks
- updated Qt to 5.9.6 on Ubuntu 16.04 and 14.04
- updated CentOS 7 to 7.5
- updated CentOS 6 to 6.10
- tested with GCC 8 and Qt 5.11 on openSUSE Tumbleweed
- updated internal boost to 1.67.0
- fixed enabling GCC/Clang C++11 and extensions
* Wed Mar 14 2018 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.9.1
- added localization test/sample app
- localization support review
- translations
- verify connect in qt solutions integration
- updated KSqueezedTextLabel to KF5
- improved DiskSpaceWidget layout
- added icon pixmap to MessageBox
- updated qt-solutions
- CoreApplicationBase::GetSupportedLanguageInfos() use app qm info
- updated Qt to 5.9.4 on Ubuntu
- updated boost to 1_66_0
- fixed meta type issues in qt solutions integration
- partial fix for KSqueezedTextLabel rich text
* Tue Jan 30 2018 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.8.1
- added GetMountPoints()
- filesystem functions quick review
- android and ios icons
- added GetMountPointsFromPath() missing implementation
* Thu Jan 18 2018 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.7.1
- qt 4 and qt 5: fixed support for qt static builds, static qico plugin, translations
* Sun Jan 7 2018 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.6.1
- added CallTraits
- added Factory
- fixed Optional test
* Fri Dec 15 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.5.1
- added Any
- added future errc
- added Optional
- this_thread Yield(), SleepFor() and SleepUntil() available even if !CPPDEVTK_HAVE_THREAD_STORAGE
- removed unnecessary exceptions
- exception classes in separate files
- exception propagation: added parameter to terminate or return null on failure
- improved TypeInfo
* Mon Nov 27 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.4.1
- added CPPDEVTK_NOEXCEPT
- added exception propagation
- added thread (not available on iOS < 9.0 and Mac OS X < 10.7 because __thread is not supported)
- added interruption support to condition variable
- added interruption support to semaphore
- Kubuntu: updated Qt to 5.9.2
- moved EnableIf and IfThenElse as Conditional in type_traits.hpp
- added more std exception classes equivalents
- treat warning "not all control paths return a value" as error
- uniform error reporting/handling in synchronization primitives
- added time utils
- removed sleep.hpp (replaced by this_thread sleep API)
- enabled console test apps on Android and iOS
- fixed internal pthread_mutex_timedlock(): absTime instead of relTime
* Tue Oct 17 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.3.1
- added generic locking algorithms
- added condition variable
- added semaphore
- android: added GetFilesDirPath()
- mutex review/cleanup
- increased iOS minimum version from 6.0 to 8.0
- internal support XCode 8 & 9
- Mac + Win: relaxed IsValidPath()
* Mon Jul 31 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.2.1
- made public on GitHub: https://github.com/cososys/cppdevtk
- packaging cleanup
- JNI review
- enabled JNI on Win32
- mutex impl .NET workaround: use QMutex even if std mutex available; maybe pImpl in the future
* Mon Jul 3 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.1.1
- Debian based packaging
- require C++11 enabled for clang and gcc >= 4.3.0
- Made ThrowOutOfMemoryErrorOrAbort() public
- mutex impl: use std mutex if available
- fixed check Qt allowed version
* Mon May 22 2017 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- v1.0.0.1
* Thu Aug 18 2016 Cristian ANITA <cristian.anita@cososys.com>, <cristian_anita@yahoo.com>
- initial package
