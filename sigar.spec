%define name	sigar
%define libname	%mklibname %{name} 0
%define devname	%mklibname %{name} -d
%define pyname	python-%{name}

%define gitdate	20100329

# Source built as:
# 	% export VERSION= 1.6.3.20100329	# date +%Y%m%d
#	% git clone git://github.com/hyperic/sigar.git sigar-$VERSION
#	% rm -fr `find sigar-$VERSION -name .git`
#	% tar jcf sigar.tar.bze sigar-$VERSION
# Note:
# building only python bindings

Name:		%{name}
Group:		Monitoring
Summary:	System Information Gatherer And Reporter
Version:	1.6.3.%{gitdate}
Release:	%mkrel 1
License:	GPL
URL:		http://support.hyperic.com/display/SIGAR/Home
Source0:	%{name}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	valgrind
%py_requires	-d

%description
The Sigar API provides a portable interface for gathering system information
such as:

    * System memory, swap, cpu, load average, uptime, logins
    * Per-process memory, cpu, credential info, state, arguments,
      environment, open files
    * File system detection and metrics
    * Network interface detection, configuration info and metrics
    * TCP and UDP connection tables
    * Network route table

#-----------------------------------------------------------------------
%package	-n %{libname}
Group:		System/Libraries
Summary:	System Information Gatherer And Reporter
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
The Sigar API provides a portable interface for gathering system information
such as:

    * System memory, swap, cpu, load average, uptime, logins
    * Per-process memory, cpu, credential info, state, arguments,
      environment, open files
    * File system detection and metrics
    * Network interface detection, configuration info and metrics
    * TCP and UDP connection tables
    * Network route table

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/libsigar.so.*

#-----------------------------------------------------------------------
%package	-n %{devname}
Group:		Development/Other
Summary:	System Information Gatherer And Reporter
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{devname}
The Sigar API provides a portable interface for gathering system information
such as:

    * System memory, swap, cpu, load average, uptime, logins
    * Per-process memory, cpu, credential info, state, arguments,
      environment, open files
    * File system detection and metrics
    * Network interface detection, configuration info and metrics
    * TCP and UDP connection tables
    * Network route table

%files		-n %{devname}
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libsigar.la
%{_libdir}/libsigar.so

#-----------------------------------------------------------------------
%package	-n %{pyname}
Group:		Development/Other
Summary:	System Information Gatherer And Reporter

%description	-n %{pyname}
The Sigar API provides a portable interface for gathering system information
such as:

    * System memory, swap, cpu, load average, uptime, logins
    * Per-process memory, cpu, credential info, state, arguments,
      environment, open files
    * File system detection and metrics
    * Network interface detection, configuration info and metrics
    * TCP and UDP connection tables
    * Network route table

%files		-n %{pyname}
%defattr(-,root,root)
%{py_platsitedir}/*

#-----------------------------------------------------------------------
%prep
%setup -q

#------------------------------------------------------------------------
%build
sh autogen.sh
%configure --disable-static --enable-shared
%make
pushd bindings/python
    python setup.py build
popd

#------------------------------------------------------------------------
%install
%makeinstall_std
pushd bindings/python
    python setup.py install --root=%{buildroot}
popd

#------------------------------------------------------------------------
%clean
rm -rf %{buildroot}
