%define upstream_name	 GraphViz
%define upstream_version 2.26
Name:		perl-%{upstream_name}
Version:	2.26
Release:	18

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ronsavage/GraphViz
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETJ/GraphViz-2.26.tar.gz

BuildRequires:	make
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
%setup -q -n GraphViz-2.26

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
make test || :

%files
%doc README
%{perl_vendorlib}/GraphViz.pm
%{perl_vendorlib}/GraphViz
%{perl_vendorlib}/Devel
%{_mandir}/*/*


