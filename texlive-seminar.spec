# revision 32762
# category Package
# catalog-ctan /macros/latex/contrib/seminar
# catalog-date 2014-01-20 13:04:19 +0100
# catalog-license lppl1.2
# catalog-version 1.61
Name:		texlive-seminar
Version:	1.61
Release:	2
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
%{_texmfdistdir}/tex/latex/seminar/sem-dem.sty
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
%{_texmfdistdir}/tex/latex/seminar/tvz-code.sty
%{_texmfdistdir}/tex/latex/seminar/tvz-hax.sty
%{_texmfdistdir}/tex/latex/seminar/tvz-user.sty
%doc %{_texmfdistdir}/doc/latex/seminar/Changes
%doc %{_texmfdistdir}/doc/latex/seminar/README
%doc %{_texmfdistdir}/doc/latex/seminar/run.sh
%doc %{_texmfdistdir}/doc/latex/seminar/sem-code.tex
%doc %{_texmfdistdir}/doc/latex/seminar/sem-make.tex
%doc %{_texmfdistdir}/doc/latex/seminar/seminar-doc.pdf
%doc %{_texmfdistdir}/doc/latex/seminar/seminar-doc.tex
%doc %{_texmfdistdir}/doc/latex/seminar/seminar.bg3
%doc %{_texmfdistdir}/doc/latex/seminar/seminar.con
%doc %{_texmfdistdir}/doc/latex/seminar/seminar.doc
%doc %{_texmfdistdir}/doc/latex/seminar/semlayer.doc
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp1.pdf
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp1.tex
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp2.pdf
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp2.tex
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp3.pdf
%doc %{_texmfdistdir}/doc/latex/seminar/semsamp3.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
