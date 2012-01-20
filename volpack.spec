%define major 1
%define libname %mklibname volpack %{major}

Name: volpack
Version: 1.0c7
Release: 1
Summary: Portable library for fast volume rendering
Group: System/Libraries
License: BSD
URL: http://amide.sourceforge.net
Source0: %{name}-%{version}.tgz
Patch0: volpack-1.0c7-mdv-link.patch

%description 
VolPack is a portable library of fast volume rendering algorithms that
produce high-quality images.  It was written by Phil Lacroute.

%package -n %{libname}
Summary: Portable library for fast volume rendering
Group: System/Libraries

%description -n %{libname}
VolPack is a portable library of fast volume rendering algorithms that
produce high-quality images.  It was written by Phil Lacroute.

%package devel
Summary: Static libraries and header file for development using volpack
Group: Development/C
Requires: volpack = %{version}

%description devel
The volpack-devel package contains the header files and static libraries
necessary for developing programs using the volpack volume rendering 
library.

%prep
%setup -q
%patch0 -p1
autoreconf

%build
%configure --enable-static=no
%make

%install
%makeinstall_std

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*so.%{major}*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/*.so
%{_includedir}/*
%{_mandir}/man3/*

