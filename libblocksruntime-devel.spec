%global builddir swift-compiler-rt-swift-DEVELOPMENT-SNAPSHOT-2018-01-12-a
Name:       libblocksruntime-devel              
Version:    4.1
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
Summary:  Development files for blocks
Provides: libblocksruntime-devel-static = %{version}-%{release}

%description devel
Development files for compiling and statically linking
blocks in a program that uses the Apple blocks
proposed extension.

%prep
tar zxf %{SOURCE0}
cp config.h %{builddir}/lib
cp buildlib %{builddir}/lib

%build
cd %{builddir}/lib
./buildlib -shared

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
install -m 644 %{builddir}/lib/BlocksRuntime/Block.h %{buildroot}/%{_includedir}
install -m 644 %{builddir}/lib/libBlocksRuntime.a %{buildroot}/%{_libdir}
install -m 644 %{builddir}/lib/libBlocksRuntime.so.0.1 %{buildroot}/%{_libdir}

%files
%defattr(-,root,root,-)
%{_libdir}/libBlocksRuntime.so.0.1

%files devel
%defattr(-,root,root,-)
%{_libdir}/libBlocksRuntime.a
%{_includedir}/Block.h

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sun Jan 14 2018 Ron Olson <tachoknight@gmail.com> 4.1-1
- Initial package for Fedora
