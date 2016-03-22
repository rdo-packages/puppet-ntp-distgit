%define upstream_name puppetlabs-ntp

Name:           puppet-ntp
Version:        XXX
Release:        XXX
Summary:        Installs, configures, and manages the NTP service.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-ntp

Source0:        https://github.com/puppetlabs/puppetlabs-ntp/archive/%{version}.tar.gz

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

