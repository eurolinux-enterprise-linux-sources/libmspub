%global apiversion 0.1

Name: libmspub
Version: 0.1.2
Release: 1%{?dist}
Summary: A library for import of Microsoft Publisher documents

License: MPLv2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libmspub
Source: http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: help2man
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(zlib)

%description
Libmspub is library providing ability to interpret and import Microsoft
Publisher content into various applications. You can find it being used
in libreoffice.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform Microsoft Publisher documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Microsoft Publisher documents into other formats.
Currently supported: XHTML, raw.

%prep
%setup -q

%build
%configure --disable-static --disable-werror --disable-silent-rules
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o pub2raw.1 ./src/conv/raw/.libs/pub2raw
help2man -N -n 'convert Publisher document into SVG' -o pub2xhtml.1 ./src/conv/svg/.libs/pub2xhtml

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
# rhbz#1001245 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 pub2*.1 %{buildroot}/%{_mandir}/man1

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
%doc docs/doxygen/html

%files tools
%{_bindir}/pub2raw
%{_bindir}/pub2xhtml
%{_mandir}/man1/pub2raw.1*
%{_mandir}/man1/pub2xhtml.1*

%changelog
* Fri Apr 17 2015 David Tardon <dtardon@redhat.com> - 0.1.2-1
- Resolves: rhbz#1207755 rebase to 0.1.2

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
