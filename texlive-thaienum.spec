%global tl_name thaienum
%global tl_revision 44140

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Thai labels in enumerate environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thaienum
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thaienum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thaienum.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides a command to use Thai numerals or characters
as labels in enumerate environments. Once the package is loaded with
\usepackage{thaienum} you can use labels such as \thainum* or
\thaimultialph* in conjunction with the package enumitem. Concrete
examples are given in the documentation.

