Name:           ros-indigo-roch-ftdi
Version:        1.0.7
Release:        0%{?dist}
Summary:        ROS roch_ftdi package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_ftdi
Source0:        %{name}-%{version}.tar.gz

Requires:       libftdi-c++-devel
Requires:       libftdi-devel
Requires:       libusb-devel
Requires:       ros-indigo-ecl-command-line
BuildRequires:  libftdi-c++-devel
BuildRequires:  libftdi-devel
BuildRequires:  libusb-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-command-line

%description
Utilities for flashing and enabling roch's USB connection. This package contains
tools for flashing the roch's FTDI chip (usually done at the factory). The
special firmware for the FTDI chip (USB to serial converter) enables it to
appear as /dev/roch on the user's PC.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 21 2017 Carl <wzhang@softrobtech.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <wzhang@softrobtech.com> - 1.0.6-1
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <wzhang@softrobtech.com> - 1.0.6-0
- Autogenerated by Bloom

