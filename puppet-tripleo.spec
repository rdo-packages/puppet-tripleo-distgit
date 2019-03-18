# add guard for OSP packages not carried
%global rhosp 0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-tripleo
Version:        8.4.1
Release:        1%{?dist}
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
Requires:       puppet-designate
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
Requires:       puppet-ovn
Requires:       puppet-oslo
Requires:       puppet-pacemaker
Requires:       puppet-panko
Requires:       puppet-rabbitmq
Requires:       puppet-redis
Requires:       puppet-remote
Requires:       puppet-rsync
Requires:       puppet-sahara
Requires:       puppet-sensu
Requires:       puppet-snmp
Requires:       puppet-ssh
Requires:       puppet-staging
Requires:       puppet-stdlib
Requires:       puppet-swift
Requires:       puppet-sysctl
Requires:       puppet-systemd
Requires:       puppet-tempest
Requires:       puppet-timezone
Requires:       puppet-tomcat
Requires:       puppet-trove
Requires:       puppet-uchiwa
Requires:       puppet-vcsrepo
Requires:       puppet-veritas_hyperscale
Requires:       puppet-vswitch
Requires:       puppet-xinetd
Requires:       puppet-zaqar
Requires:       puppet-zookeeper
Requires:       puppet >= 2.7.0

%if 0%{rhosp} == 0
Requires:       puppet-mongodb
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
* Mon Mar 18 2019 RDO <dev@lists.rdoproject.org> 8.4.1-1
- Update to 8.4.1

* Fri Feb 15 2019 RDO <dev@lists.rdoproject.org> 8.4.0-1
- Update to 8.4.0

* Wed Aug 08 2018 RDO <dev@lists.rdoproject.org> 8.3.5-1
- Update to 8.3.5

* Mon Jul 09 2018 RDO <dev@lists.rdoproject.org> 8.3.4-1
- Update to 8.3.4

* Mon Jun 04 2018 RDO <dev@lists.rdoproject.org> 8.3.3-1
- Update to 8.3.3

* Mon Apr 23 2018 RDO <dev@lists.rdoproject.org> 8.3.2-1
- Update to 8.3.2

* Tue Mar 27 2018 Jon Schlueter <jschluet@redhat.com> 8.3.1-1
- Update to 8.3.1

* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 8.3.0-1
- Update to 8.3.0



