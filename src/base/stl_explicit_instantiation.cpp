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


#define CPPDEVTK_BASE_STL_EXPLICIT_INSTANTIATION_CPP


#include <cppdevtk/base/stl_explicit_instantiation.hpp>


namespace cppdevtk {
namespace base {


#if (CPPDEVTK_ENABLE_TIOS_EXPL_INST)
template class CPPDEVTK_BASE_API ::std::basic_ios<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_ios<wchar_t, ::std::char_traits<wchar_t> >;
#endif


#if (CPPDEVTK_ENABLE_TISTREAM_EXPL_INST)
template class CPPDEVTK_BASE_API ::std::basic_istream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_istream<wchar_t, ::std::char_traits<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_iostream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_iostream<wchar_t, ::std::char_traits<wchar_t> >;
#endif


#if (CPPDEVTK_ENABLE_TOSTREAM_EXPL_INST)
template class CPPDEVTK_BASE_API ::std::basic_ostream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_ostream<wchar_t, ::std::char_traits<wchar_t> >;
#endif


#if (CPPDEVTK_ENABLE_TSSTREAM_EXPL_INST)

template class CPPDEVTK_BASE_API ::std::basic_stringbuf<char, ::std::char_traits<char>,
		::std::allocator<char> >;
template class CPPDEVTK_BASE_API ::std::basic_stringbuf<wchar_t, ::std::char_traits<wchar_t>,
		::std::allocator<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_istringstream<char, ::std::char_traits<char>,
		::std::allocator<char> >;
template class CPPDEVTK_BASE_API ::std::basic_istringstream<wchar_t, ::std::char_traits<wchar_t>,
		::std::allocator<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_ostringstream<char, ::std::char_traits<char>,
		::std::allocator<char> >;
template class CPPDEVTK_BASE_API ::std::basic_ostringstream<wchar_t, ::std::char_traits<wchar_t>,
		::std::allocator<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_stringstream<char, ::std::char_traits<char>,
		::std::allocator<char> >;
template class CPPDEVTK_BASE_API ::std::basic_stringstream<wchar_t, ::std::char_traits<wchar_t>,
		::std::allocator<wchar_t> >;

#endif


#if (CPPDEVTK_ENABLE_TSTREAMBUF_EXPL_INST)
template class CPPDEVTK_BASE_API ::std::basic_streambuf<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_streambuf<wchar_t, ::std::char_traits<wchar_t> >;
#endif


#if (CPPDEVTK_ENABLE_TSTRING_EXPL_INST)

template struct CPPDEVTK_BASE_API ::std::char_traits<char>;
template struct CPPDEVTK_BASE_API ::std::char_traits<wchar_t>;

template class CPPDEVTK_BASE_API ::std::allocator<char>;
template class CPPDEVTK_BASE_API ::std::allocator<wchar_t>;

template class CPPDEVTK_BASE_API ::std::basic_string<char, ::std::char_traits<char>,
		::std::allocator<char> >;
template class CPPDEVTK_BASE_API ::std::basic_string<wchar_t, ::std::char_traits<wchar_t>,
		::std::allocator<wchar_t> >;

#endif


#if (CPPDEVTK_ENABLE_TFSTREAM_EXPL_INST)

template class CPPDEVTK_BASE_API ::std::basic_filebuf<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_filebuf<wchar_t, ::std::char_traits<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_ifstream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_ifstream<wchar_t, ::std::char_traits<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_ofstream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_ofstream<wchar_t, ::std::char_traits<wchar_t> >;

template class CPPDEVTK_BASE_API ::std::basic_fstream<char, ::std::char_traits<char> >;
template class CPPDEVTK_BASE_API ::std::basic_fstream<wchar_t, ::std::char_traits<wchar_t> >;

#endif


}	// namespace base
}	// namespace cppdevtk
