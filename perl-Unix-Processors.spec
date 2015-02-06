%define upstream_name    Unix-Processors
%define upstream_version 2.042

Summary:	Interface to processor (CPU) information
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:        GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/UNIX/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Perl interface to processor (CPU) information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.42.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.42.0-2mdv2011.0
+ Revision: 555209
- rebuild

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 2.42.0-1mdv2010.1
+ Revision: 495435
- update to 2.042

* Fri Jan 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 2.41.0-1mdv2010.1
+ Revision: 484783
- import perl-Unix-Processors


