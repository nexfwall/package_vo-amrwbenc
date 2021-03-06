Name:			vo-amrwbenc
Version:		0.1.3
Release:		2%{?dist}
Summary:		VisualOn AMR-WB encoder library
Group:			System Environment/Libraries
License:		ASL 2.0
URL:			http://opencore-amr.sourceforge.net/
Source0:		http://downloads.sourceforge.net/opencore-amr/%{name}/%{name}-%{version}.tar.gz

%description
This library contains an encoder implementation of the Adaptive 
Multi Rate Wideband (AMR-WB) audio codec. The library is based 
on a codec implementation by VisualOn as part of the Stagefright 
framework from the Google Android project.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT 
rm $RPM_BUILD_ROOT%{_libdir}/libvo-amrwbenc.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README NOTICE
%{_libdir}/libvo-amrwbenc.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libvo-amrwbenc.so
%{_libdir}/pkgconfig/vo-amrwbenc.pc

%changelog
* Sun Apr 10 2016 Egor Zaharov <nexfwall@gmail.com> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 Michael Kuhn <suraia@ikkoku.de> - 0.1.3-1
- Update to 0.1.3.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Sep 16 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.1.2-1
- New upstream release 0.1.2
- Drop static lib
- Some spec-file cleanups

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 04 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 0.1.1-1
- upgraded to new version 0.1.1

* Wed May 04 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 0.1.0-1
- Initial build
