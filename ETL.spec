Summary:	Voria Extended Class and Template Library
Summary(pl.UTF-8):	Biblioteka rozszerzeń klas i wzorców Vorii
Name:		ETL
Version:	0.04.17
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/synfig/%{name}-%{version}.tar.gz
# Source0-md5:	fe59e0b56d9fbeb255de658d920ebefd
URL:		http://www.synfig.org/
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VoriaETL is a multiplatform class and template library designed to
complement and supplement the C++ STL.

%description -l pl.UTF-8
VoriaETL jest wieloplatformową biblioteką klas i wzorców przeznaczoną
do uzupełniania STL C++.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ETL-config
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
