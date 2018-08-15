%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-ntp
%global commit 4.2.x
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-ntp
Version:        4.2.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages the NTP service.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-ntp

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 4.2.0-1.4.2.xgit
- Update to post 4.2.0 (4.2.x)


