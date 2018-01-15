%global builddir swift-compiler-rt-swift-DEVELOPMENT-SNAPSHOT-2018-01-12-a
%global shlibver 0.1
Name:       libblocksruntime
Version:    4.1
Group:      Development/Libraries
Release:    1%{?dist}
Summary:    The BlocksRuntime development files from Apple's compiler-rt project
License:    MIT
URL:        https://github.com/apple/swift-compiler-rt
Source0:    https://github.com/apple/swift-compiler-rt/archive/swift-DEVELOPMENT-SNAPSHOT-2018-01-12-a.tar.gz
Source1:    buildlib
Source2:    config.h

BuildRequires: gcc-c++

%description
This package contains development headers for building 
software that uses blocks, a proposed extension to the 
C, Objective C, and C++ languages developed by Apple 
to support the Grand Central Dispatch concurrency engine.

%package devel
Group:      Development/Libraries
Summary:    Development files for blocks
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for compiling and statically linking
blocks in a program that uses the Apple blocks
proposed extension.

%package static
Summary:    Static development file for libblocksruntime
Group:      Development/Libraries
Requires:   %{name}-devel = %{version}-%{release}

%description static
This package contains the static library to develop
applications that use libblocksruntime

%prep
tar zxf %{SOURCE0}
cp config.h %{builddir}/lib
cp buildlib %{builddir}/lib

%build
cd %{builddir}/lib
./buildlib -shared

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 644 %{builddir}/lib/BlocksRuntime/Block.h %{buildroot}%{_includedir}
install -m 644 %{builddir}/lib/libBlocksRuntime.a %{buildroot}%{_libdir}
install -m 644 %{builddir}/lib/libBlocksRuntime.so.%{shlibver} %{buildroot}/%{_libdir}
ln -fs libBlocksRuntime.so.%{shlibver} %{buildroot}%{_libdir}/libBlocksRuntime.so.0
ln -fs libBlocksRuntime.so.0 %{buildroot}%{_libdir}/libBlocksRuntime.so

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%license %{builddir}/LICENSE.TXT

%files devel
%defattr(-,root,root,-)
%{_includedir}/Block.h
%{_libdir}/*.so

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Sun Jan 14 2018 Ron Olson <tachoknight@gmail.com> 4.1-1
- Initial package for Fedora
