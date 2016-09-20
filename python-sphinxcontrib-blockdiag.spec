# Created by pyp2rpm-3.1.3
%global pypi_name sphinxcontrib-blockdiag

Name:           python-%{pypi_name}
Version:        1.5.5
Release:        1%{?dist}
Summary:        Sphinx "blockdiag" extension

License:        BSD
URL:            https://github.com/blockdiag/sphinxcontrib-blockdiag
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel

%description
 sphinxcontribblockdiag A sphinx extension for embedding block diagram using
blockdiag_.This extension enables you to insert block diagrams into your
document. Following code is an example:: .. blockdiag:: diagram { A > B > C; B
> D; .. _blockdiag: For more details, see online documentation_ at _online
documentation:

%package -n     python2-%{pypi_name}
Summary:        Sphinx "blockdiag" extension
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-blockdiag >= 1.5.0
Requires:       python-Sphinx >= 0.6
%description -n python2-%{pypi_name}
 sphinxcontribblockdiag A sphinx extension for embedding block diagram using
blockdiag_.This extension enables you to insert block diagrams into your
document. Following code is an example:: .. blockdiag:: diagram { A > B > C; B
> D; .. _blockdiag: For more details, see online documentation_ at _online
documentation:


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/sphinxcontrib
%{python2_sitelib}/sphinxcontrib_blockdiag-*.egg-info
%{python2_sitelib}/sphinxcontrib_blockdiag-*.pth

%changelog
* Tue Sep 20 2016 Ricardo Noriega <rnoriega@redhat.com> - 1.5.5-1
- Initial package.
