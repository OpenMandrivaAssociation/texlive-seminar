# revision 18322
# category Package
# catalog-ctan /macros/latex/contrib/seminar
# catalog-date 2010-05-17 14:53:01 +0200
# catalog-license lppl1.2
# catalog-version 1.5
Name:		texlive-seminar
Version:	1.5
Release:	1
Summary:	Make overhead slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/seminar
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seminar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seminar.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/seminar/npsfont.sty
%{_texmfdistdir}/tex/latex/seminar/sem-a4.sty
%{_texmfdistdir}/tex/latex/seminar/sem-page.sty
%{_texmfdistdir}/tex/latex/seminar/semcolor.sty
%{_texmfdistdir}/tex/latex/seminar/semhelv.sty
%{_texmfdistdir}/tex/latex/seminar/seminar.bg2
%{_texmfdistdir}/tex/latex/seminar/seminar.bug
%{_texmfdistdir}/tex/latex/seminar/seminar.cls
%{_texmfdistdir}/tex/latex/seminar/seminar.sty
%{_texmfdistdir}/tex/latex/seminar/semlayer.sty
%{_texmfdistdir}/tex/latex/seminar/semlcmss.sty
%{_texmfdistdir}/tex/latex/seminar/semrot.sty
%{_texmfdistdir}/tex/latex/seminar/slidesec.sty
%doc %{_texmfdistdir}/doc/latex/seminar/read-me.2e
%doc %{_texmfdistdir}/doc/latex/seminar/sem-read.me
%doc %{_texmfdistdir}/doc/latex/seminar/sem-user.pdf
%doc %{_texmfdistdir}/doc/latex/seminar/sem-user.tex
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp1.tex
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp2.tex
%doc %{_texmfdistdir}/doc/latex/seminar/tvz-code.sty
%doc %{_texmfdistdir}/doc/latex/seminar/tvz-hax.sty
%doc %{_texmfdistdir}/doc/latex/seminar/tvz-user.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
