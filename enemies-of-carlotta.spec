Summary:	A simple mailing list manager
Summary:	Prosty zarz�dca list pocztowych
Name:		enemies-of-carlotta
Version:	1.0.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://liw.iki.fi/liw/eoc/%{name}-%{version}.tar.gz
# Source0-md5:	c128776396562ef1c678e438422d11fb
Patch0:		%{name}-DESTDIR.patch
URL:		http://liw.iki.fi/liw/eoc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enemies of Carlotta is a simple mailing list manager. It tries to
mimick the ezmlm software somewhat, but is written completely from
scratch, in Python. It also has nicer license.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	man1dir=%{_mandir}/man1 \
	man1dirfr=%{_mandir}/fr/man1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARKS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%lang(fr) %{_mandir}/fr/man1/*