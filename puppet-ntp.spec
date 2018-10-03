%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-ntp


Name:           puppet-ntp
Version:        4.2.0
Release:        2%{?dist}
Summary:        Installs, configures, and manages the NTP service.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-ntp

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{upstream_version}.tar.gz
BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages the NTP service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ntp/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ntp/



%files
%{_datadir}/openstack-puppet/modules/ntp/


%changelog
* Wed Oct 03 2018 Jon Schlueter <jschluet@redhat.org> 4.2.0-2
- rebuild to reflect that we are at 4.2.0 tag on 4.2.x branch

* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 4.2.0-1.4.2.xgit
- Update to post 4.2.0 (4.2.x)
