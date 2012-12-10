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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20080321-4mdv2011.0
+ Revision: 620148
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20080321-3mdv2010.0
+ Revision: 429795
- rebuild

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080321-2mdv2009.0
+ Revision: 239236
- build as a shared library too, and fix compile flags
- import liblinebreak


* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 20080321-1mdv2009.0
- first mdv release, using package from Antony Dovgal <tony@daylessday.org> 
