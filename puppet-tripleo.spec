%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-tripleo
Version:        6.5.14
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
* Mon Jul 09 2018 RDO <dev@lists.rdoproject.org> 6.5.14-1
- Update to 6.5.14

* Thu May 31 2018 RDO <dev@lists.rdoproject.org> 6.5.13-1
- Update to 6.5.13

* Mon Apr 23 2018 RDO <dev@lists.rdoproject.org> 6.5.12-1
- Update to 6.5.12

* Tue Mar 27 2018 RDO <dev@lists.rdoproject.org> 6.5.11-1
- Update to 6.5.11

* Wed Mar 07 2018 RDO <dev@lists.rdoproject.org> 6.5.10-1
- Update to 6.5.10

* Thu Feb 08 2018 RDO <dev@lists.rdoproject.org> 6.5.9-1
- Update to 6.5.9

* Thu Jan 25 2018 RDO <dev@lists.rdoproject.org> 6.5.8-1
- Update to 6.5.8

* Mon Jan 08 2018 RDO <dev@lists.rdoproject.org> 6.5.7-1
- Update to 6.5.7

* Sat Dec 09 2017 RDO <dev@lists.rdoproject.org> 6.5.6-1
- Update to 6.5.6

* Tue Nov 14 2017 RDO <dev@lists.rdoproject.org> 6.5.5-1
- Update to 6.5.5

* Fri Nov 03 2017 RDO <dev@lists.rdoproject.org> 6.5.4-1
- Update to 6.5.4

* Tue Oct 10 2017 rdo-trunk <javier.pena@redhat.com> 6.5.3-1
- Update to 6.5.3

* Thu Oct 05 2017 rdo-trunk <javier.pena@redhat.com> 6.5.2-1
- Update to 6.5.2

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


