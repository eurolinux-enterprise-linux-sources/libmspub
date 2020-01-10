%global apiversion 0.0

Name: libmspub
Version: 0.0.6
Release: 3%{?dist}
Summary: A library providing ability to interpret and import Microsoft Publisher files

Group: System Environment/Libraries
License: GPLv2+ or LGPLv2+ or MPLv1.1
URL: http://www.freedesktop.org/wiki/Software/libmspub
Source: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: libicu-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: zlib-devel

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform Microsoft Publisher files into other formats
Group: Applications/Publishing
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Publisher files into other formats.
Currently supported: XHTML, raw.


%prep
%setup -q


%build
%configure --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING.*
%{_libdir}/%{name}-%{apiversion}.so.*


%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc


%files doc
%doc COPYING.*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html


%files tools
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.0.6-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.6-2
- Mass rebuild 2013-12-27

* Tue May 14 2013 David Tardon <dtardon@redhat.com> - 0.0.6-1
- new release

* Wed Feb 20 2013 David Tardon <dtardon@redhat.com> - 0.0.5-1
- new release

* Wed Jan 30 2013 David Tardon <dtardon@redhat.com> - 0.0.4-1
- new release

* Fri Aug 24 2012 David Tardon <dtardon@redhat.com> - 0.0.3-1
- new release

* Fri Jul 27 2012 David Tardon <dtardon@redhat.com> - 0.0.2-3
- rebuilt for boost 1.50

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 David Tardon <dtardon@redhat.com> - 0.0.2-1
- Resolves: rhbz#840445 new release

* Thu Jul 12 2012 David Tardon <dtardon@redhat.com> 0.0.1-1
- new release

* Thu Jun 07 2012 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
