Name:           ros-kinetic-roch-base
Version:        2.0.15
Release:        0%{?dist}
Summary:        ROS roch_base package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roch_base
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-angles
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-diff-drive-controller
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roch-control
Requires:       ros-kinetic-roch-description
Requires:       ros-kinetic-roch-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-roch-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf

%description
Sawyer Roch robot driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Sep 19 2017 Carl <wzhang@softrobtech.com> - 2.0.15-0
- Autogenerated by Bloom

* Mon Sep 18 2017 Carl <wzhang@softrobtech.com> - 2.0.14-0
- Autogenerated by Bloom

* Thu Mar 30 2017 Carl <wzhang@softrobtech.com> - 2.0.13-2
- Autogenerated by Bloom

* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-1
- Autogenerated by Bloom

* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-0
- Autogenerated by Bloom

