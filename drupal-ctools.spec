%define modname		ctools
%define drupal_version	7
%define module_version	1.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Chaos tool suite module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
BuildArch:	noarch

%description
This suite is primarily a set of APIs and tools to improve the developer
experience. It also contains a module called the Page Manager whose job is to
manage pages. In particular it manages panel pages, but as it grows it will be
able to manage far more than just Panels.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc API.txt CHANGELOG.txt


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.1-1
+ Revision: 813180
- update to 7.x.1.1

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.0-1
+ Revision: 798246
- imported package drupal-ctools

