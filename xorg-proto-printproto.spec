# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	Xprint extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xprint
Name:		xorg-proto-printproto
Version:	1.0.5
Release:	2.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/printproto-%{version}.tar.bz2
# Source0-md5:	99d0e25feea2fead7d8325b7000b41c3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xprint extension to the X11 protocol is (now deprecated) portable,
network-transparent printing system.

%description -l pl.UTF-8
Rozszerzenie Xprint protokołu X11 jest (teraz już przestarzałym)
systemem drukowania przezroczystym względem sieci.

%package devel
Summary:	Xprint extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Xprint
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Xprint extension to the X11 protocol is (now deprecated) portable,
network-transparent printing system.

%description devel -l pl.UTF-8
Rozszerzenie Xprint protokołu X11 jest (teraz już przestarzałym)
systemem drukowania przezroczystym względem sieci.

%prep
%setup -q -n printproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/Print*.h
%{_pkgconfigdir}/printproto.pc
%{_mandir}/man7/Xprint.7*
