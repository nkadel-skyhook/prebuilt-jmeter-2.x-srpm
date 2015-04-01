Summary: Apache Jmeter
Name: prebuilt-jmeter
Version: 2.13
Release: 0.1%{?dist}
License: Apache
Group: Applications/Internet
Source: apache-jmeter-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Provides: apache-jmeter = %{version}-%{release}
Provides: jmeter = %{version}-%{release}
Requires: java

%description
Apache Jmeter is a pure Java performance tester for web services, databases,
email, and middleware.

%prep
%setup -q -n apache-jmeter-%{version}

%build
install --directory ${RPM_BUILD_ROOT}

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}/opt/jmeter-%{version}
cp -a . ${RPM_BUILD_ROOT}/opt/jmeter-%{version}
ln -s --no-dereference jmeter-%{version} ${RPM_BUILD_ROOT}/opt/jmeter

install --directory ${RPM_BUILD_ROOT}/etc/profile.d
cat > /etc/profile.d/jmeter.sh << EOF
PATH=$PATH:/opt/jmeter/bin
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%license LICENSE
%doc README NOTICE
/opt/jmeter-%{version}
/opt/jmeter
%config /etc/profile.d/jmeter.sh

%changelog
* Wed Apr 01 2015 Nico Kadel-Garcia <nkadel@skyhookwireless.com - 2.13-0.1
- Original wrapper for pre-built jmeter
