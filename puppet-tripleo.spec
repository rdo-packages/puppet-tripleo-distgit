%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-tripleo
Version:        6.5.1
Release:        1%{?dist}
Summary:        TripleO Puppet Module
License:        ASL 2.0

URL:            https://github.com/openstack/puppet-tripleo

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-cassandra
Requires:       puppet-zookeeper
Requires:       puppet-firewall
Requires:       puppet-midonet
Requires:       puppet-tomcat
Requires:       puppet-keepalived
Requires:       puppet-haproxy
Requires:       puppet-systemd
Requires:       puppet >= 2.7.0

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
* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 6.5.1-1
- Update to 6.5.1

* Wed Jun 28 2017 rdo-trunk <javier.pena@redhat.com> 6.5.0-1
- Update to 6.5.0

* Fri Apr 28 2017 rdo-trunk <javier.pena@redhat.com> 6.4.0-1
- Update to 6.4.0

* Mon Mar 06 2017 Alfredo Moralejo <amoralej@redhat.com> 6.3.0-1
- Update to 6.3.0

* Thu Feb 16 2017 Alfredo Moralejo <amoralej@redhat.com> 6.2.0-1
- Update to 6.2.0


