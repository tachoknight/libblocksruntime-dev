%define builddir swift-compiler-rt-swift-DEVELOPMENT-SNAPSHOT-2018-01-12-a
Name:       libblocksruntime-dev		
Version:	4.1
Release:	1%{?dist}
BuildRoot:  %{_tmppath}/%{name}-%{version}
Summary:	The BlocksRuntime development files from Apple's compiler-rt project
License:	MIT
URL:		https://github.com/apple/swift-compiler-rt
Source0:	https://github.com/apple/swift-compiler-rt/archive/swift-DEVELOPMENT-SNAPSHOT-2018-01-12-a.tar.gz
Source1:    buildlib
Source2:    config.h

BuildRequires: gcc-c++

%description
The blocks runtime todo create better description

%prep
tar zxf %{SOURCE0}
cp config.h %{builddir}/lib
cp buildlib %{builddir}/lib

%build
cd %{builddir}/lib
./buildlib

%install
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
install -m 755 %{builddir}/lib/libBlocksRuntime.a %{buildroot}/%{_libdir}
install -m 755 %{builddir}/lib/BlocksRuntime/Block.h %{buildroot}/%{_includedir}


%files
%{_libdir}/libBlocksRuntime.a
%{_includedir}/Block.h


%changelog
* Sun Jan 14 2018 Ron Olson <tachoknight@gmail.com> 4.1-1
- Initial package for Fedora
