Summary:	A simple mailing list manager
Summary(pl.UTF-8):   Prosty zarządca list pocztowych
Name:		enemies-of-carlotta
Version:	1.1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://liw.iki.fi/liw/eoc/%{name}-%{version}.tar.gz
# Source0-md5:	34e6e943b9305500c19ad77fbf7e64a5
URL:		http://liw.iki.fi/liw/eoc/
Requires:	procmail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enemies of Carlotta is a simple mailing list manager. It tries to
mimick the ezmlm software somewhat, but is written completely from
scratch, in Python. It also has nicer license.

%description -l pl.UTF-8
Enemies of Carlotta jest prostym zarządcą list pocztowych. Próbuje
naśladować trochę ezmlma, jednak jest napisany całkowicie od zera w
Pythonie. Posiada także bardziej przyjazną licencję.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	man1dir=%{_mandir}/man1 \
	man1dirfr=%{_mandir}/fr/man1 \
	man1dires=%{_mandir}/es/man1 \
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
%lang(es) %{_mandir}/es/man1/*
