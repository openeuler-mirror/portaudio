Name:           portaudio
Version:        19
Release:        30
Summary:        Free, cross platform, open-source, audio I/O library
License:        MIT
URL:            http://www.portaudio.com/
Source0:        http://www.portaudio.com/archives/pa_stable_v19_20140130.tgz
Patch0000:      portaudio-doxynodate.patch
Patch0001:      portaudio-pkgconfig-alsa.patch
BuildRequires:  doxygen alsa-lib-devel jack-audio-connection-kit-devel autoconf automake libtool

%description
PortAudio is a portable audio I/O library that uses a callback
mechanism to request audio processing.Audio can be generated in
multiple formats.

%package        devel
Summary:        Development files for the portaudio audio I/O library
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains files required to build applications that will use the
portaudio library.

%prep
%autosetup -n %{name} -p1
autoreconf -i -f

%build
%configure --disable-static --enable-cxx
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' bindings/cpp/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' bindings/cpp/libtool
make
doxygen

%install
%make_install

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%license LICENSE.txt
%doc README.txt
%{_libdir}/*.so.*

%files devel
%doc doc/html/*
%{_includedir}/portaudiocpp/
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Fri Sep 03 2021 wangyue<wangyue92@huawei.com> - 19-30
- release number add 1

* Thu Nov 14 2019 wangye<wangye54@huawei.com> - 19-29
- Package init
