%global debug_package %{nil}
%global shlibver 1


Name:       libblocksruntime
Version:    5.0.1
Release:    1%{?dist}
Summary:    LLVM's compiler-rt/BlocksRuntime development files 
License:    NCSA and MIT
URL:        http://compiler-rt.llvm.org
Source0:    http://releases.llvm.org/5.0.1/compiler-rt-5.0.1.src.tar.xz
Source1:    buildlib
Source2:    config.h

BuildRequires: gcc

%description
This package contains development headers for building 
software that uses blocks, a proposed extension to the 
C, Objective C, and C++ languages developed by Apple 
to support the Grand Central Dispatch concurrency engine.

%package devel
Summary:    Development files for blocks
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for compiling and statically linking
blocks in a program that uses the Apple blocks
proposed extension.

%package static
Summary:    Static development file for libblocksruntime
Requires:   %{name}-devel = %{version}-%{release}

%description static
This package contains the static library to develop
applications that use libblocksruntime

%prep
%setup -n compiler-rt-%{version}.src
cp -p %SOURCE1 lib
cp -p %SOURCE2 lib

%build
cd lib
./buildlib -shared %{shlibver}

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -m 644 lib/BlocksRuntime/Block.h %{buildroot}%{_includedir}
install -m 644 lib/libBlocksRuntime.a %{buildroot}%{_libdir}
install -m 755 lib/libBlocksRuntime.so.0.%{shlibver} %{buildroot}/%{_libdir}
ln -fs libBlocksRuntime.so.0.%{shlibver} %{buildroot}%{_libdir}/libBlocksRuntime.so.0
ln -fs libBlocksRuntime.so.0 %{buildroot}%{_libdir}/libBlocksRuntime.so

%files
%license LICENSE.TXT
%{_libdir}/*.so.*

%files devel
%{_includedir}/Block.h
%{_libdir}/*.so

%files static
%{_libdir}/*.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Sun Jan 14 2018 Ron Olson <tachoknight@gmail.com> 5.0.1-1
- Initial package for Fedora
