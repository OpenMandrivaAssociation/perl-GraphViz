%define upstream_name	 GraphViz
%define upstream_version 2.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	graphviz
BuildRequires:	perl(Math::Bezier)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Graph)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/GraphViz.pm
%{perl_vendorlib}/GraphViz
%{perl_vendorlib}/Devel
%{_mandir}/*/*
