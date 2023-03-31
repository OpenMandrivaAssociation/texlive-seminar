Name:		texlive-seminar
Version:	59801
Release:	2
Summary:	Make overhead slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/seminar
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seminar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seminar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class that produces overhead slides (transparencies), with
many facilities. The class requires availability of the
fancybox package. Seminar is also the basis of other classes,
such as prosper. In fact, seminar is not nowadays reckoned a
good basis for a presentation -- users are advised to use more
recent classes such as powerdot or beamer, both of which are
tuned to 21st-century presentation styles. Note that the
seminar distribution relies on the xcomment package, which was
once part of the bundle, but now has a separate existence.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/seminar
%doc %{_texmfdistdir}/doc/latex/seminar

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
