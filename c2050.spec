Name:           c2050
Version:        0.3b
Release:        3.1%{?dist}
Summary:        Converts bitcmyk data to Lexmark 2050 printer language

Group:          System Environment/Libraries
License:        GPL+
URL:            http://www.prato.linux.it/~mnencia/lexmark2050/
Source0:        http://www.prato.linux.it/~mnencia/lexmark2050/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is a filter to convert bitcmyk data such as produced by ghostscript to
the printer language of Lexmark 2050 printers.  It is meant to be used
by the PostScript Description files of the drivers from the foomatic package.

%prep
%setup -q

%build
# The included Makefile is badly written
%{__cc} %{optflags} -o c2050 c2050.c

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} c2050 $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/c2050
%doc COPYING README

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.3b-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.3b-1
- New upstream, just integrates the signedness patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3a-4
- Autorebuild for GCC 4.3

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.3a-3
- Modify the License tag in accordance with the new guidelines

* Mon Jun 11 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.3a-2
- Silence the %%setup (#243947)

* Mon Jun 11 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.3a-1
- Upstream added missing copyright notice upon request
- Patch for correcting signedness issues on some Archs

* Thu Jun 7 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.3-1
- Initial package
