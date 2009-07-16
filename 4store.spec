Summary:	Fast RDF quad store
Name:		4store
Version:	0.9.2
Release:	1
License:	LGPL v2+
Group:		Applications/Databases
Source0:	http://4store.org/download/%{name}-v%{version}.tar.gz
# Source0-md5:	40cff8523f2bcff56d2ee6f826fec43d
URL:		http://4store.org/
Patch0:		%{name}-prefix.patch
Patch1:		%{name}-termcap.patch
Patch2:		%{name}-destdir.patch
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
4store is a database storage and query engine that holds RDF data. It
has been used by Garlik as their primary RDF platform for three years,
and has proved itself to be robust and secure.

4store's main strengths are it's performance, scalability and
stability. It does not provide many features over and above RDF
storage and SPARQL queries, but if your are looking for a scalable,
secure, fast and efficient RDF store, then 4store should be on your
shortlist.

%package devel
Summary:	Header files for 4store libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliote4store
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for 4store libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek 4store.

%package static
Summary:	Static 4store libraries
Summary(pl.UTF-8):	Statyczne biblioteki 4store
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static 4store libraries.

%description static -l pl.UTF-8
Statyczne biblioteki 4store.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO docs/*
%attr(755,root,root) %{_bindir}/4s*
%{_mandir}/man1/*.1.*

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
