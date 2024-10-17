%define upstream_name	 GraphViz
%define upstream_version 2.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	graphviz
BuildRequires:	perl(Math::Bezier)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Graph)
BuildArch:	noarch
Requires:	graphviz

%description
This module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato" and "twopi" programs from the GraphViz
project (http://www.graphviz.org/ or
http://www.research.att.com/sw/tools/graphviz/). 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc README
%{perl_vendorlib}/GraphViz.pm
%{perl_vendorlib}/GraphViz
%{perl_vendorlib}/Devel
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.0
+ Revision: 402138
- rebuild using %%perl_convert_version

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdv2009.1
+ Revision: 314246
- update to new version 2.04

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.03-3mdv2009.0
+ Revision: 257132
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2008.1
+ Revision: 110398
- update to new version 2.03

* Sun Sep 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-5mdv2008.0
+ Revision: 88421
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-4mdv2007.0
- Rebuild

* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-3mdv2007.0
- Rebuild

* Mon Jan 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-2mdk
- spec cleanup
- %%mkrel
- better URL

* Thu Jan 13 2005 Guillaume Rousse <guillomovitch@mandrake.org> 2.02-1mdk 
- new release
- back in official contrib

* Thu Sep 30 2004 Guillaume Rousse <guillomovitch@zarb.org> 2.01-1plf
- New release 2.01

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@zarb.org> 2.00-1plf
- New release 2.00

* Wed Aug 25 2004 Guillaume Rousse <guillomovitch@zarb.org> 1.9-1plf
- new version 
- PLF transfer
- requires graphviz
- no more explicit perl requires
- fixed buildrequires

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.8-4mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.8-3mdk
- fixed dir ownership (distlint)
- %%makeinstall_std macro

