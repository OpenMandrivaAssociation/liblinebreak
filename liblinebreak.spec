%define major %version
%define libname	  %mklibname linebreak %{major}
%define develname %mklibname -d linebreak

Name: 		liblinebreak
Summary: 	Line breaking in a Unicode sequence
Version:	20080321
Release: 	%mkrel 4
License: 	GPL
Group:		System/Libraries
URL: 		http://vimgadgets.cvs.sourceforge.net/vimgadgets/common/tools/linebreak/
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
Provides:   linebreak-devel
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Line breaking in a Unicode sequence. 
Designed to be used in a generic text renderer.

%prep
%setup -q

%build
%make  CC=%__cc CFLAGS="%{optflags} -fPIC" CFG=release
%__cc \
    -shared -Wl,-soname,liblinebreak.so.%{major} \
    -o liblinebreak.so.%{version} \
    ReleaseDir/*.o

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}
install -d -m 755 %{buildroot}%{_includedir}
install -m 755 liblinebreak.so.%{version} %{buildroot}%{_libdir}
install -m 644 ReleaseDir/liblinebreak.a %{buildroot}%{_libdir}
install -m 644 linebreak.h %{buildroot}%{_includedir}

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblinebreak.so.%{major}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/liblinebreak.a
%{_includedir}/linebreak.h

