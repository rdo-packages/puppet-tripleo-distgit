%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-tripleo
Version:        5.6.9
Release:        1%{?dist}
Summary:        TripleO Puppet Module
License:        Apache-2.0

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
* Tue Mar 27 2018 RDO <dev@lists.rdoproject.org> 5.6.9-1
- Update to 5.6.9

* Thu Mar 08 2018 RDO <dev@lists.rdoproject.org> 5.6.8-1
- Update to 5.6.8

* Tue Jan 23 2018 RDO <dev@lists.rdoproject.org> 5.6.7-1
- Update to 5.6.7

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 5.6.6-1
- Update to 5.6.6

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 5.6.5-1
- Update to 5.6.5

* Wed Oct 11 2017 rdo-trunk <javier.pena@redhat.com> 5.6.4-1
- Update to 5.6.4

* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 5.6.3-1
- Update to 5.6.3

* Mon Sep 04 2017 rdo-trunk <javier.pena@redhat.com> 5.6.2-1
- Update to 5.6.2

* Thu Apr 27 2017 rdo-trunk <javier.pena@redhat.com> 5.6.0-1
- Update to 5.6.0

* Tue Jan 03 2017 Alan Pevec <alan.pevec@redhat.com> 5.5.0-1
- Update to 5.5.0
- CVE-2016-9599 Enforce Firewall TCP / UDP rules management

* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 5.4.0-1
- Update to 5.4.0

* Tue Oct 18 2016 Alfredo Moralejo <amoralej@redhat.com> 5.3.0-1
- Update to 5.3.0

* Thu Sep 29 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.2.0-1
- Update to 5.2.0

* Fri Sep 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.1.0-1
- Update to 5.1.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 5.0.0-1
- Update to 5.0.0


