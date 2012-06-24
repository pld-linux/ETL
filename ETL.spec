Summary:	Voria Extended Class and Template Library
Summary(pl):	Biblioteka rozszerze� klas i wzorc�w Vorii
Name:		ETL
Version:	0.04.08
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.bridgetone.com/voria/files/%{name}-%{version}.tar.gz
# Source0-md5:	610f00117c2d0e088030a0956242bd1c
URL:		http://www.synfig.com/download
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VoriaETL is a multiplatform class and template library designed to
complement and supplement the C++ STL.

%description -l pl
VoriaETL jest wieloplatformow� bibliotek� klas i wzorc�w przeznaczon�
do uzupe�niania STL C++.

%prep
%setup -q

%build
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
