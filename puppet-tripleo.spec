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

Requires:       puppet-aodh
Requires:       puppet-apache
Requires:       puppet-auditd
Requires:       puppet-barbican
Requires:       puppet-cassandra
Requires:       puppet-ceilometer
Requires:       puppet-ceph
Requires:       puppet-certmonger
Requires:       puppet-cinder
Requires:       puppet-collectd
Requires:       puppet-concat
Requires:       puppet-contrail
Requires:       puppet-corosync
Requires:       puppet-datacat
Requires:       puppet-ec2api
Requires:       puppet-elasticsearch
Requires:       puppet-fdio
Requires:       puppet-firewall
Requires:       puppet-fluentd
Requires:       puppet-git
Requires:       puppet-glance
Requires:       puppet-gnocchi
Requires:       puppet-haproxy
Requires:       puppet-heat
Requires:       puppet-horizon
Requires:       puppet-inifile
Requires:       puppet-ipaclient
Requires:       puppet-ironic
Requires:       puppet-java
Requires:       puppet-kafka
Requires:       puppet-keepalived
Requires:       puppet-keystone
Requires:       puppet-kibana3
Requires:       puppet-kmod
Requires:       puppet-manila
Requires:       puppet-memcached
Requires:       puppet-midonet
Requires:       puppet-mistral
Requires:       puppet-module-data
Requires:       puppet-mongodb
Requires:       puppet-mysql
Requires:       puppet-n1k-vsm
Requires:       puppet-neutron
Requires:       puppet-nova
Requires:       puppet-nssdb
Requires:       puppet-ntp
Requires:       puppet-octavia
Requires:       puppet-opendaylight
Requires:       puppet-openstack_extras
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet-systemd
Requires:       puppet-tomcat
Requires:       puppet-veritas_hyperscale
Requires:       puppet-zookeeper
Requires:       puppet >= 2.7.0

%if 0%{rhosp} == 0
Requires:       puppet-congress
Requires:       puppet-etcd
Requires:       puppet-qdr
Requires:       puppet-tacker
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


