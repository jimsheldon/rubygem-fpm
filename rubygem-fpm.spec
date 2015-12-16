# Generated from fpm-1.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname fpm

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: fpm - package building and mangling
Name: rubygem-%{gemname}
Version: 1.4.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT-like
URL: https://github.com/jordansissel/fpm
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: rubygem(json) >= 1.7.7
Requires: rubygem(cabin) >= 0.6.0
Requires: rubygem(backports) >= 2.6.2
Requires: rubygem(arr-pm) => 0.0.10
Requires: rubygem(arr-pm) < 0.1
Requires: rubygem(clamp) => 0.6
Requires: rubygem(clamp) < 1
Requires: rubygem(childprocess) 
Requires: rubygem(ffi) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Convert directories, rpms, python eggs, rubygems, and more to rpms, debs,
solaris packages and more. Win at package management without wasting pointless
hours debugging bad rpm specs!


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%dir %{geminstdir}
%{_bindir}/fpm
%{geminstdir}/bin
%{geminstdir}/lib
%{geminstdir}/.require_paths
%{geminstdir}/CHANGELIST
%{geminstdir}/CONTRIBUTORS
%{geminstdir}/LICENSE
%{geminstdir}/templates
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Dec 16 2015 Jim Sheldon <jim.sheldon@meltwater.com> - 1.4.0-1
- Initial package
