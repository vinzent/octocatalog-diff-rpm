%global __provides_exclude ^python.*$

Name:           vinzent-octocatalog-diff
Version:        1.3.0
Release:        0.0.1%{?dist}
Summary:        Compile Puppet catalogs from 2 branches, versions, etc., and compare them

License:        Apache 2.0
URL:            https://github.com/vinzent/octocatalog-diff-rpm
Source0:        https://github.com/vinzent/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rubygem-bundler, ruby-devel, make, cmake, gcc

%description
octocatalog-diff is a tool that enables developers to be more 
efficient when testing changes to Puppet manifests. It is most
commonly used to display differences in Puppet catalogs between
stable and development branches. It does not require a working 
Puppet master (or puppetserver), so it is often run by 
developers on their workstations and in Continuous Integration 
environments.


%prep
%setup -q

%build
echo "BUILD $(pwd)"

%install
mkdir -p $RPM_BUILD_ROOT/opt/vinzent/octocatalog-diff
cp Gemfile $RPM_BUILD_ROOT/opt/vinzent/octocatalog-diff
cd $RPM_BUILD_ROOT/opt/vinzent/octocatalog-diff

bundle install --binstubs bin/ --standalone

find ./ -name "gem_make.out" -delete
find ./ -name "*.log" -delete
find ./ -name "*.o" -delete
find ./ -type d -name build -exec rm -rf {} +


%files
/opt/vinzent/octocatalog-diff

%changelog
