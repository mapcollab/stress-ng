Summary: stress-ng
Name: stress-ng
Version: 0.05.22
Release: 1
Group: System Environment/Libraries
URL: http://kernel.ubuntu.com/~cking/stress-ng/
License: GPLv2
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz


%description
stress-ng will stress test a computer system in various selectable ways. It
was designed to exercise various physical subsystems of a computer as well as
the various operating system kernel interfaces.


%prep
%setup -q -n %{name}-%{version}


%build
make


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 stress-ng            %{buildroot}/%{_bindir}/


%files
%attr(0755,root,root) %{_bindir}/stress-ng


%changelog
