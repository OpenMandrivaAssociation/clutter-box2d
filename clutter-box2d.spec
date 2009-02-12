Name:           clutter-box2d
Version:        0.8.2
Release:        %mkrel 1
Summary:        Glue layer between clutter and box2d
Group:          Development/C
License:        LGPLv2+
URL:            http://www.clutter-project.org
Source0:        http://www.clutter-project.org/sources/%{name}/0.8/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  clutter-devel >= 0.8.0

%description
This allows clutter to be embedded in cairo applications. 

%package devel
Summary:        Clutter-box2d development environment
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
clutter-box2d

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f %buildroot%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libclutter-box2d-0.8.so.0
%{_libdir}/libclutter-box2d-0.8.so.0.*
%doc %{_datadir}/gtk-doc/html/clutter-box2d

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/clutter-box2d-0.8.pc
%{_libdir}/libclutter-box2d-0.8.so
%{_includedir}/clutter-0.8/clutter-box2d

