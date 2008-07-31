%define module	GraphViz
%define name	perl-%{module}
%define version 2.03
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/L/LB/LBROCARD/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Requires:	graphviz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Math::Bezier)
BuildRequires:	perl(IPC::Run)
BuildRequires:	perl(Graph)
BuildRequires:	graphviz
BuildRequires:	fonts-ttf-dejavu
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato" and "twopi" programs from the GraphViz
project (http://www.graphviz.org/ or
http://www.research.att.com/sw/tools/graphviz/). 

%prep
%setup -q -n %{module}-%{version}

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

