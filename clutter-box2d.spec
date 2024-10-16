%define major 0
%define api 0.10
%define clutterapi 1.0
%define libname %mklibname %name _%api %major
%define develname %mklibname -d %name _%api
Name:           clutter-box2d
Version:        0.10.0
Release:        %mkrel 8
Summary:        Glue layer between clutter and box2d
Group:          Graphics
License:        LGPLv2+
URL:            https://www.clutter-project.org
Source0:        http://www.clutter-project.org/sources/%{name}/%api/%{name}-%{version}.tar.bz2
Patch: clutter-box2d-0.10.0-new-gobject-introspection.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  clutter-devel >= 1.0
BuildRequires:  gobject-introspection-devel gir-repository

%description
This allows clutter to be embedded in cairo applications. 

%package -n %libname
Summary:       Glue layer between clutter and box2d
Group:         System/Libraries

%description -n %libname
This allows clutter to be embedded in cairo applications. 

%package -n %develname
Summary:        Clutter-box2d development environment
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description -n %develname
Header files and libraries for building a extension library for the
clutter-box2d

%prep
%setup -q
%patch -p1 -b .new-gobject-introspection
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f %buildroot%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS README
%{_libdir}/libclutter-box2d-%api.so.%{major}*
%_libdir/girepository-1.0/ClutterBox2D-%api.typelib

%files -n %develname
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/clutter-box2d
%{_libdir}/pkgconfig/clutter-box2d-%api.pc
%{_libdir}/libclutter-box2d-%api.so
%{_includedir}/clutter-%clutterapi/clutter-box2d
%_datadir/gir-1.0/ClutterBox2D-%api.gir


