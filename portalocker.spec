#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE81444E9CE1F695D (wolph@wol.ph)
#
Name     : portalocker
Version  : 1.7.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/7a/75/47453988b56b400fc73083123b15ac48f8488deec3d1060e3956dd03ee4e/portalocker-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/75/47453988b56b400fc73083123b15ac48f8488deec3d1060e3956dd03ee4e/portalocker-1.7.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/7a/75/47453988b56b400fc73083123b15ac48f8488deec3d1060e3956dd03ee4e/portalocker-1.7.0.tar.gz.asc
Summary  : Wraps the portalocker recipe for easy usage
Group    : Development/Tools
License  : Python-2.0
Requires: portalocker-license = %{version}-%{release}
Requires: portalocker-python = %{version}-%{release}
Requires: portalocker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
portalocker - Cross-platform locking library
        ############################################

%package license
Summary: license components for the portalocker package.
Group: Default

%description license
license components for the portalocker package.


%package python
Summary: python components for the portalocker package.
Group: Default
Requires: portalocker-python3 = %{version}-%{release}

%description python
python components for the portalocker package.


%package python3
Summary: python3 components for the portalocker package.
Group: Default
Requires: python3-core
Provides: pypi(portalocker)

%description python3
python3 components for the portalocker package.


%prep
%setup -q -n portalocker-1.7.0
cd %{_builddir}/portalocker-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603398990
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/portalocker
cp %{_builddir}/portalocker-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/portalocker/63e1288b0ebc7a7a559b2939a4f5f9a7ee2e673f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/portalocker/63e1288b0ebc7a7a559b2939a4f5f9a7ee2e673f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
