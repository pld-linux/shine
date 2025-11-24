#
# Conditional build:
%bcond_without	static_libs	# static libraries

Summary:	Fixed-point MP3 encoding library
Summary(pl.UTF-8):	Biblioteka stałoprzecinkowego kodowania MP3
Name:		shine
Version:	3.1.1
Release:	1
# COPYING says so, no other licensing information found
License:	LGPL v2
Group:		Libraries
#Source0Download: https://github.com/toots/shine/releases
Source0:	https://github.com/savonet/shine/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ff41cb139c25470f2d9c9acc9f97cc8d
URL:		https://github.com/savonet/shine/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixed-point MP3 encoding library.

%description -l pl.UTF-8
Biblioteka stałoprzecinkowego kodowania MP3.

%package devel
Summary:	Header files for shine library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki shine
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for shine library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki shine.

%package static
Summary:	Static shine library
Summary(pl.UTF-8):	Statyczna biblioteka shine
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static shine library.

%description static -l pl.UTF-8
Statyczna biblioteka shine.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{__enable_disable static_libs static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md README.old
%attr(755,root,root) %{_bindir}/shineenc
%attr(755,root,root) %{_libdir}/libshine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libshine.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libshine.so
%{_includedir}/shine
%{_pkgconfigdir}/shine.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libshine.a
%endif
