# add guard for OSP packages not carried
%global rhosp 0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-tripleo
Version:        XXX
Release:        XXX
Summary:        TripleO Puppet Module
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-tripleo

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-fdio
Requires:       puppet-stdlib
Requires:       puppet-cassandra
Requires:       puppet-zookeeper
Requires:       puppet-firewall
Requires:       puppet-midonet
Requires:       puppet-tomcat
Requires:       puppet-keepalived
Requires:       puppet-haproxy
Requires:       puppet-systemd
Requires:       puppet-veritas_hyperscale
Requires:       puppet >= 2.7.0

%if 0%{rhosp} == 0
Requires:       puppet-etcd
Requires:       puppet-qdr
%endif


%description
Lightweight composition layer for Puppet TripleO.

%prep
%setup -q -n openstack-tripleo-%{upstream_version}

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

