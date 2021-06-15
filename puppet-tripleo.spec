%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da
# add guard for OSP packages not carried
%global rhosp 0
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           puppet-tripleo
Version:        14.1.0
Release:        1%{?dist}
Summary:        TripleO Puppet Module
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-tripleo

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

Requires:       puppet-aodh >= 13.0.0
Requires:       puppet-apache
Requires:       puppet-auditd
Requires:       puppet-barbican >= 13.0.0
Requires:       puppet-cassandra
Requires:       puppet-ceilometer >= 13.0.0
Requires:       puppet-certmonger
Requires:       puppet-cinder >= 13.0.0
Requires:       puppet-collectd
Requires:       puppet-concat
Requires:       puppet-contrail
Requires:       puppet-corosync
Requires:       puppet-datacat
Requires:       puppet-designate >= 13.0.0
Requires:       puppet-ec2api >= 13.0.0
Requires:       puppet-elasticsearch
Requires:       puppet-etcd
Requires:       puppet-fdio
Requires:       puppet-firewall
Requires:       puppet-git
Requires:       puppet-glance >= 13.0.0
Requires:       puppet-gnocchi >= 13.0.0
Requires:       puppet-haproxy
Requires:       puppet-heat >= 13.0.0
Requires:       puppet-horizon >= 13.0.0
Requires:       puppet-inifile
Requires:       puppet-ipaclient
Requires:       puppet-ironic >= 13.0.0
Requires:       puppet-java
Requires:       puppet-kafka
Requires:       puppet-keepalived
Requires:       puppet-keystone >= 13.0.0
Requires:       puppet-kibana3
Requires:       puppet-kmod
Requires:       puppet-manila >= 13.0.0
Requires:       puppet-memcached
Requires:       puppet-midonet
Requires:       puppet-mistral >= 13.0.0
Requires:       puppet-module-data
Requires:       puppet-mysql
Requires:       puppet-n1k-vsm
Requires:       puppet-neutron >= 13.0.0
Requires:       puppet-nova >= 13.0.0
Requires:       puppet-nssdb
Requires:       puppet-octavia >= 13.0.0
Requires:       puppet-openstack_extras >= 13.0.0
Requires:       puppet-openstacklib >= 13.0.0
Requires:       puppet-ovn >= 13.0.0
Requires:       puppet-oslo >= 13.0.0
Requires:       puppet-pacemaker
Requires:       puppet-placement
Requires:       puppet-qdr
Requires:       puppet-rabbitmq
Requires:       puppet-redis
Requires:       puppet-remote
Requires:       puppet-rsync
Requires:       puppet-rsyslog
Requires:       puppet-sahara >= 13.0.0
Requires:       puppet-snmp
Requires:       puppet-ssh
Requires:       puppet-staging
Requires:       puppet-stdlib
Requires:       puppet-swift >= 13.0.0
Requires:       puppet-sysctl
Requires:       puppet-systemd
Requires:       puppet-timezone
Requires:       puppet-tomcat
Requires:       puppet-vcsrepo
Requires:       puppet-veritas_hyperscale
Requires:       puppet-vswitch >= 9.0.0
Requires:       puppet-xinetd
Requires:       puppet-zaqar >= 13.0.0
Requires:       puppet-zookeeper
%if 0%{?fedora}
# NOTE(bogdando): only needed for f28-based CI passing,
# remove this condition for the "else" path, once we have Centos 8.
Requires:       puppet-headless >= 5.5.6
%else
Requires:       puppet-headless >= 5.5.10
%endif
# NOTE(aschultz): needed to properly manage firewall rules.
Requires:       iptables-services
%if 0%{?fedora} || 0%{?rhel} > 7
# NOTE(aschultz): needed for rabbitmq on rhel8/fedora, see LP#1822673
# https://review.openstack.org/#/c/649170/
Requires:       glibc-langpack-en
%endif

%if 0%{rhosp} == 0
Requires:       puppet-mongodb
%endif


%description
Lightweight composition layer for Puppet TripleO.

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Wed May 05 2021 RDO <dev@lists.rdoproject.org> 14.1.0-1
- Update to 14.1.0

