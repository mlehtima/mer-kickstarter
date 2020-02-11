# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       mer-kickstarter
Summary:    Create kickstart files for Mer images
Version:    0
Release:    1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        http://www.merproject.org
Source0:    %{name}-%{version}.tar.gz
Requires:   python3-yaml
Requires:   python3-urlgrabber
Requires:   python3-cheetah
Requires:   python3-lxml
BuildRequires:  python3-base
BuildRequires:  python3-cheetah

%description
Create Configuration files to build Mer images

%prep
%setup -q -n %{name}-%{version}

%build
make tmpls

CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
rm -rf %{buildroot}
%{__python3} setup.py install --root=%{buildroot} -O1

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{python3_sitearch}/*
