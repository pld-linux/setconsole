Summary:	Sets the system to use either a local terminal or a serial console
Summary(pl.UTF-8):	Narzędzie włączające korzystanie z lokalnego terminala lub konsoli szeregowej
Name:		setconsole
Version:	1.0
Release:	10
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	033f9096417977a2e9d3bce55788c302
Patch0:		%{name}-1.0.patch
Patch1:		%{name}-fix.patch
Requires:	grep
Requires:	sed
Requires:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
ExclusiveOS:	Linux

%description
Setconsole is a basic system utility for setting up the /etc/inittab,
/dev/systty and /dev/console files to handle a new console. The
console can be either the local terminal (i.e., directly attached to
the system via a video card) or a serial console.

%description -l pl.UTF-8
setconsole to narzędzie systemowe do ustawiania /etc/inittab,
/dev/systty i /dev/console do obsługi nowej konsoli. Konsola może być
lokalnym terminalem (bezpośrednio podłączonym przez kartę graficzną)
lub szeregowa.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

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
