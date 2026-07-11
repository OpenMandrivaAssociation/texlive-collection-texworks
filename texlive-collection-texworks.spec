%global tl_name collection-texworks
%global tl_revision 71515

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeXworks editor; TL includes only the Windows binary
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-texworks
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-texworks.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(collection-basic)
Requires:	texlive(texworks)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
See https://tug.org/texworks.

