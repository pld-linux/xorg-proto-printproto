Summary:	Print protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Print i pomocnicze
Name:		xorg-proto-printproto
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/printproto-%{version}.tar.bz2
# Source0-md5:	0f4e7982c6d4ec3b2cf38502dd1293a3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Print protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Print i pomocnicze.

%package devel
Summary:	Print protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Print i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Print protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Print i pomocnicze.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/printproto.pc
