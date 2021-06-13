%global abi_package %{nil}

Name:           granite
Summary:        elementary companion library for GTK+ and GLib
Version:        6.0.0
Release:        1
License:        LGPLv3+
URL:            https://github.com/elementary/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  appstream-glib
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Requires:       gsettings-desktop-schemas
Requires:       hicolor-icon-theme

%description    
Granite is a companion library for GTK+ and GLib.

%package        dev
Summary:        Granite Toolkit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    dev
Dev headers for Granite.

%prep
%setup

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang granite

%files -f granite.lang
%doc README.md
%license COPYING

%{_libdir}/libgranite.so*
%{_libdir}/girepository-1.0/Granite-1.0.typelib
%{_datadir}/icons/hicolor/*/actions/appointment.svg
%{_datadir}/icons/hicolor/*/actions/open-menu.svg
%{_datadir}/icons/hicolor/scalable/actions/open-menu-symbolic.svg
%{_datadir}/metainfo/%{name}.appdata.xml


%files dev
%doc README.md
%license COPYING
%{_bindir}/granite-demo
%{_libdir}/libgranite.so
%{_libdir}/pkgconfig/granite.pc
%{_includedir}/granite/
%{_datadir}/applications/io.elementary.granite.demo.desktop
%{_datadir}/gir-1.0/Granite-1.0.gir
%{_datadir}/vala/vapi/granite.deps
%{_datadir}/vala/vapi/granite.vapi


%changelog
# based on https://koji.fedoraproject.org/koji/packageinfo?packageID=23477
