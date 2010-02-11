Summary:	Free TrueType font for the Yi script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma yi
Name:		fonts-TTF-Sil-Nuosu
Version:	2.1.1
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
# Source0Download:	http://scripts.sil.org/cms/SCRIPTs/render_download.php?site_id=nrsi&format=file&media_id=NuosuSIL2.1.1.zip&filename=NuosuSIL2.1.1.zip
Source0:	NuosuSIL%{version}.zip
# Source0-md5:	50570ee6e8d5a8f338ab7d95f3c9eee5
URL:		http://scripts.sil.org/cms/SCRIPTs/page.php?site_id=nrsi&item_id=SILYI_home
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The Nuosu SIL Font is a single Unicode font for the standardized Yi
script used by a large ethnic group in southwestern China.

%prep
%setup -q -n NuosuSIL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{ttffontsdir}/NuosuSIL.ttf
