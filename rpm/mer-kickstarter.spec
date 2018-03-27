Name:       mer-kickstarter

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Summary:    Create kickstart files for Mer images
Version:    0
Release:    1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://www.merproject.org
Source0:    %{name}-%{version}.tar.gz
Requires:   python-yaml
Requires:   python-urlgrabber
Requires:   python-cheetah
Requires:   python-lxml
BuildRequires:  pkgconfig(python-2.7)
BuildRequires:  python-cheetah

%description
Create Configuration files to build Mer images

%prep
%setup -q -n %{name}-%{version}

%build
make tmpls

CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} -O1

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{python_sitelib}/*
