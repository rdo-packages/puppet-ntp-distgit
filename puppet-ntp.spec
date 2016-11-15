%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-ntp

Name:           puppet-ntp
Version:        4.2.0
Release:        2%{?dist}
Summary:        Installs, configures, and manages the NTP service.
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 4.2.0-2
- Newton update 4.2.0 (93da3bd01a5ae4276eddec15ac615eb4bccc23cf)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 4.2.0-1.d93d4b6.git
- Newton update 4.2.0 (d93d4b66c6818c9a7281d5af173bbde582fd299c)


