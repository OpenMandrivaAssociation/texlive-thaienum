Name:		texlive-thaienum
Version:	44140
Release:	2
Summary:	Thai labels in enumerate environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thaienum
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thaienum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thaienum.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides a command to use Thai numerals or
characters as labels in enumerate environments. Once the
package is loaded with \usepackage{thaienum} you can use labels
such as \thainum* or \thaimultialph* in conjunction with the
package enumitem. Concrete examples are given in the
documentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/thaienum
%doc %{_texmfdistdir}/doc/latex/thaienum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
