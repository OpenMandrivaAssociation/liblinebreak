%define major %(echo %{version} |cut -d. -f1)
%define libname	  %mklibname linebreak
%define develname %mklibname -d linebreak
%define staticname %mklibname -d -s linebreak

Name: 		liblinebreak
Summary: 	Line breaking in a Unicode sequence
Version:	2.1
Release: 	1
License: 	GPL
Group:		System/Libraries
URL: 		https://vimgadgets.cvs.sourceforge.net/vimgadgets/common/tools/linebreak/
Source0: 	https://cyfuture.dl.sourceforge.net/project/vimgadgets/liblinebreak/%{version}/liblinebreak-%{version}.tar.gz
BuildSystem:	autotools
BuildOption:	--enable-static

%description
Line breaking in a Unicode sequence. 
Designed to be used in a generic text renderer.

%package -n %{libname}
Summary: 	Line breaking in a Unicode sequence
Group:		System/Libraries

%description -n %{libname}
Line breaking in a Unicode sequence. 
Designed to be used in a generic text renderer.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Provides:	linebreak-devel
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Line breaking in a Unicode sequence. 
Designed to be used in a generic text renderer.

%package -n %{staticname}
Summary:	Static library for developing programs that will use %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
Line breaking in a Unicode sequence. 
Designed to be used in a generic text renderer.

%files -n %{libname}
%{_libdir}/liblinebreak.so.%{major}*

%files -n %{develname}
%{_includedir}/linebreak.h
%{_includedir}/linebreakdef.h
%{_libdir}/liblinebreak.so

%files -n %{staticname}
%{_libdir}/liblinebreak.a
