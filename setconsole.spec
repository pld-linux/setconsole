Summary:	Sets the system to use either a local terminal or a serial console.
Name:		setconsole
Version:	1.0
Release:	9
Copyright:	GPL
Group:		Applications/System
Source:		setconsole-1.0.tar.gz
Patch:		setconsole-1.0.patch
Exclusiveos:	Linux
Requires:	/bin/sh textutils grep sed
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArchitectures: noarch

%description
Setconsole is a basic system utility for setting up the /etc/inittab,
/dev/systty and /dev/console files to handle a new console.  The
console can be either the local terminal (i.e., directly attached to
the system via a video card) or a serial console.

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install setconsole $RPM_BUILD_ROOT%{_sbindir}/setconsole
install setconsole.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/setconsole
%{_mandir}/man8/setconsole.8*
