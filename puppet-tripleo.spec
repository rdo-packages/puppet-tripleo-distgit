Name:           puppet-tripleo
Version:        XXX
Release:        XXX
Summary:        TripleO Puppet Module
License:        Apache-2.0

URL:            https://github.com/openstack/puppet-tripleo

Source0: 	http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-cassandra
Requires:       puppet-zookeeper
Requires:       puppet-firewall
Requires:       puppet-midonet
Requires:       puppet-tomcat
Requires:       puppet-keepalived
Requires:       puppet-haproxy
Requires:       puppet >= 2.7.0

%description
Lightweight composition layer for Puppet TripleO.

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/tripleo/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/tripleo/



%files
%{_datadir}/openstack-puppet/modules/tripleo/


%changelog

