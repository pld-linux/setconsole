Summary:	Sets the system to use either a local terminal or a serial console
Summary(pl):	Narzêdzie w³±czaj±ce korzystanie z lokalnego terminala lub konsoli szeregowej
Name:		setconsole
Version:	1.0
Release:	9
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-1.0.patch
ExclusiveOS:	Linux
Requires:	/bin/sh textutils grep sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Setconsole is a basic system utility for setting up the /etc/inittab,
/dev/systty and /dev/console files to handle a new console. The
console can be either the local terminal (i.e., directly attached to
the system via a video card) or a serial console.

%description -l pl
setconsole to narzêdzie systemowe do ustawiania /etc/inittab,
/dev/systty i /dev/console do obs³ugi nowej konsoli. Konsola mo¿e byæ
lokalnym terminalem (bezpo¶rednio pod³±czonym przez kartê graficzn±)
lub szeregowa.

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install setconsole $RPM_BUILD_ROOT%{_sbindir}/setconsole
install setconsole.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/setconsole
%{_mandir}/man8/setconsole.8*
