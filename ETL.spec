Summary:	Voria Extended Class and Template Library
Summary(pl.UTF-8):	Biblioteka rozszerzeń klas i wzorców Vorii
Name:		ETL
Version:	0.04.10
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/synfig/ETL-0.04.10.tar.gz
# Source0-md5:	2eb64b0737f62988dd89367cee8c9b55
Patch0:	%{name}-crazy-debugging.patch
URL:		http://www.synfig.com/download
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
%patch0 -p1

%build
. "config/build.cfg"

SED_SCRIPT="
s/@PACKAGE@/$PACKAGE/g;
s/@PACKAGE_NAME@/$PACKAGE_NAME/g;
s/@PACKAGE_BUGREPORT@/$PACKAGE_BUGREPORT/g;
s/@PACKAGE_TARNAME@/$PACKAGE_TARNAME/g;
s/@PACKAGE_VERSION@/$PACKAGE_VERSION/g;
s|@SVN_REPOSITORY@|$SVN_REPOSITORY|g;
s/@VERSION@/$VERSION/g;
s/@API_VERSION@/$API_VERSION/g;
s/@VERSION_MAJ@/$VERSION_MAJ/g;
s/@VERSION_MIN@/$VERSION_MIN/g;
s/@VERSION_REV@/$VERSION_REV/g;
s/@VERSION_REL@/$VERSION_REL/g;
s/@CFLAGS@//g;
"
for FILENAME in doxygen.cfg pkgconfig.pc; do 
	sed "$SED_SCRIPT" < "config/$FILENAME.in" > $FILENAME;
done

mv pkgconfig.pc "$PACKAGE_TARNAME.pc.in"

sed "$SED_SCRIPT" < "config/configure.ac" > configure.in

%{__libtoolize}
%{__aclocal} -I config
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
