Summary: Sets the system to use either a local terminal or a serial console.
Name: setconsole
Version: 1.0
Release: 8
Copyright: GPL
Group: Applications/System
Source: setconsole-1.0.tar.gz
Patch: setconsole-1.0.patch
Exclusiveos: Linux
Requires: /bin/sh textutils grep sed
BuildArchitectures: noarch
BuildRoot: /var/tmp/setconsole-root

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
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,man/man8}

install -m755 setconsole $RPM_BUILD_ROOT/usr/sbin/setconsole
install -m644 setconsole.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/setconsole
/usr/man/man8/setconsole.8
