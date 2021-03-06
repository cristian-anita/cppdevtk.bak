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


#ifndef CPPDEVTK_UTIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_HPP_INCLUDED_
#define CPPDEVTK_UTIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_HPP_INCLUDED_


#include "config.hpp"
#include <cppdevtk/util/filesystem_exception.hpp>
#include <cppdevtk/base/unused.hpp>


namespace cppdevtk {
namespace util {


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// \addtogroup exceptions
/// @{


#define CPPDEVTK_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION()	\
	::cppdevtk::util::NoSuchFileOrDirectoryException(CPPDEVTK_SOURCE_CODE_INFO())

#define CPPDEVTK_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_W_P(path)	\
	::cppdevtk::util::NoSuchFileOrDirectoryException(CPPDEVTK_SOURCE_CODE_INFO(), (path))


#define CPPDEVTK_MAKE_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION(excName)	\
	::cppdevtk::util::NoSuchFileOrDirectoryException excName(CPPDEVTK_SOURCE_CODE_INFO())

#define CPPDEVTK_MAKE_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_W_P(excName, path)	\
	::cppdevtk::util::NoSuchFileOrDirectoryException excName(CPPDEVTK_SOURCE_CODE_INFO(), (path))


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/// Thrown to indicate that file/directory does not exists.
class CPPDEVTK_UTIL_API NoSuchFileOrDirectoryException: public FilesystemException {
public:
	explicit NoSuchFileOrDirectoryException(const ::cppdevtk::base::SourceCodeInfo& throwPoint);
	NoSuchFileOrDirectoryException(const ::cppdevtk::base::SourceCodeInfo& throwPoint, const QString& path);
	
	virtual ~NoSuchFileOrDirectoryException() CPPDEVTK_NOEXCEPT;
	
	::std::auto_ptr<NoSuchFileOrDirectoryException> Clone() const;
	
#	if (CPPDEVTK_COMPILER_HAVE_MVI_CRT_BUG)
	virtual QtException* clone() const;
#	else
	virtual NoSuchFileOrDirectoryException* clone() const;
#	endif
	
	void Swap(NoSuchFileOrDirectoryException& other) CPPDEVTK_NOEXCEPT;
	
	QString GetPath() const;
	void SetPath(const QString& path);
protected:
	virtual void DoThrow() const;
	
#	if (CPPDEVTK_COMPILER_HAVE_MVI_CRT_BUG)
	virtual ::cppdevtk::base::Cloneable* DoClone() const;
#	else
	virtual NoSuchFileOrDirectoryException* DoClone() const;
#	endif
	
	void SwapOwnData(NoSuchFileOrDirectoryException& other) CPPDEVTK_NOEXCEPT;
};


CPPDEVTK_UTIL_API void swap(NoSuchFileOrDirectoryException& x, NoSuchFileOrDirectoryException& y) CPPDEVTK_NOEXCEPT;


/// @}
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Inline functions

#define CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG "no such file or directory"

inline NoSuchFileOrDirectoryException::NoSuchFileOrDirectoryException(const ::cppdevtk::base::SourceCodeInfo& throwPoint):
		Exception(throwPoint), RuntimeException(throwPoint, CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG),
		SystemException(throwPoint, MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory),
		CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG),
		IosFailureException(throwPoint, CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG,
		MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory)),
		FilesystemException(throwPoint, MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory),
		CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG) {}

inline NoSuchFileOrDirectoryException::NoSuchFileOrDirectoryException(const ::cppdevtk::base::SourceCodeInfo& throwPoint,
		const QString& path): Exception(throwPoint), RuntimeException(throwPoint, CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG),
		SystemException(throwPoint, MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory),
		CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG),
		IosFailureException(throwPoint, CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG,
		MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory)),
		FilesystemException(throwPoint, MakeErrorCode(::cppdevtk::base::errc::no_such_file_or_directory),
		CPPDEVTK_DETAIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_MSG, path) {}

inline NoSuchFileOrDirectoryException::~NoSuchFileOrDirectoryException() CPPDEVTK_NOEXCEPT {}

inline ::std::auto_ptr<NoSuchFileOrDirectoryException> NoSuchFileOrDirectoryException::Clone() const {
	return ::std::auto_ptr<NoSuchFileOrDirectoryException>(dynamic_cast<NoSuchFileOrDirectoryException*>(
			Cloneable::Clone().release()));
}

#if (CPPDEVTK_COMPILER_HAVE_MVI_CRT_BUG)
inline QtException* NoSuchFileOrDirectoryException::clone() const {
#else
inline NoSuchFileOrDirectoryException* NoSuchFileOrDirectoryException::clone() const {
#endif
	return Clone().release();
}

inline void NoSuchFileOrDirectoryException::Swap(NoSuchFileOrDirectoryException& other) CPPDEVTK_NOEXCEPT {
	if (this != &other) {
		FilesystemException::Swap(other);
		SwapOwnData(other);
	}
}

inline QString NoSuchFileOrDirectoryException::GetPath() const {
	return GetSrcPath();
}

inline void NoSuchFileOrDirectoryException::SetPath(const QString& path) {
	SetSrcPath(path);
}

inline void NoSuchFileOrDirectoryException::DoThrow() const {
	throw *this;
}

#if (CPPDEVTK_COMPILER_HAVE_MVI_CRT_BUG)
inline ::cppdevtk::base::Cloneable* NoSuchFileOrDirectoryException::DoClone() const {
#else
inline NoSuchFileOrDirectoryException* NoSuchFileOrDirectoryException::DoClone() const {
#endif
	return new NoSuchFileOrDirectoryException(*this);
}

inline void NoSuchFileOrDirectoryException::SwapOwnData(NoSuchFileOrDirectoryException& other) CPPDEVTK_NOEXCEPT {
	::cppdevtk::base::SuppressUnusedWarning(other);
}


inline CPPDEVTK_UTIL_API void swap(NoSuchFileOrDirectoryException& x, NoSuchFileOrDirectoryException& y) CPPDEVTK_NOEXCEPT {
	x.Swap(y);
}


}	// namespace util
}	// namespace cppdevtk


#endif	// CPPDEVTK_UTIL_NO_SUCH_FILE_OR_DIRECTORY_EXCEPTION_HPP_INCLUDED_
