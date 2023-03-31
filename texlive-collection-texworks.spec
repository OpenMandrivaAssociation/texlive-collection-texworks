Name:		texlive-collection-texworks
Version:	54074
Release:	2
Summary:	TeXworks editor; TL includes only the Windows binary
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collection-texworks
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-texworks.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
See http://tug.org/texworks.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
