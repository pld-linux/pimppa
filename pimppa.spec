Summary:	A toolkit to hoard binaries
Summary(pl):	Zestaw narzêdzi do zbierania binariów
Name:		pimppa
Version:	0.5.2
Release:	2
License:	GPL
Group:		Networking/News
Group(de):	Netzwerkwesen/News
Group(pl):	Sieciowe/News
Source0:	http://download.sourceforge.net/pimppa/%{name}-%{version}.tar.gz
Requires:	suck >= 4.2.2
Requires:	mysql >= 3.22.30
Requires:	uudeview >= 0.5.13
URL:		http://pimppa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
Buildrequires:	mysql-devel >= 3.22.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PIMPPA automates leeching files from newsgroups and FTP sites, with
decoding, duplicate discarding, simple spam skip heuristics, sorting
to predefined directories and further file processing. The keyword is
"minimal user interaction".

It is NOT a newsreader or ftp client, and can't be used for manual
article reading or site browsing.

%description -l pl
PIMPPA automatyzuje ¶ci±ganie plików z grup usenetowych i serwerów
FTP, wraz z dekodowaniem, usuwaniem duplikatów, heurystycznym
pomijaniem spamu, sortowaniem do predefiniowanych katalalogów i dalsz±
obróbk± plików. S³owem kluczowym jest "minimalna interakcja
u¿ytkownika".

To NIE jest czytnik newsów ani klient ftp, nie mo¿e byæ u¿ywany do
rêcznego czytania postów ani przegl±dania serwerów.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf FAQ README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if mysqlshow -u pimppa pimppa 1>/dev/null 2>/dev/null ; then
	echo
	echo "It seems you're upgrading, as pimppa MySQL tables seem to"
	echo "already exist. I won't recreate them."
	echo
	echo You MUST read %{_defaultdocdir}/%{name}-%{version}/ChangeLog to see 
	echo if you have to perform some actions manually in this upgrade.
	echo
	echo
else
	echo
	echo Installing PIMPPA MySQL database, db user and tables.
	OLDDIR=`pwd`
	cd %{_datadir}/pimppa/extras
	/bin/sh ./createdb
	cd $OLDDIR
fi

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/padddir
%attr(755,root,root) %{_bindir}/padopt
%attr(755,root,root) %{_bindir}/passign
%attr(755,root,root) %{_bindir}/pbackup
%attr(755,root,root) %{_bindir}/pcfg
%attr(755,root,root) %{_bindir}/pchkfn
%attr(755,root,root) %{_bindir}/pclean
%attr(755,root,root) %{_bindir}/pdesc
%attr(755,root,root) %{_bindir}/pf
%attr(755,root,root) %{_bindir}/prm
%attr(755,root,root) %{_bindir}/pleech
%attr(755,root,root) %{_bindir}/pmarkoff
%attr(755,root,root) %{_bindir}/pmd5sum
%attr(755,root,root) %{_bindir}/pmv
%attr(755,root,root) %{_bindir}/pmv3
%attr(755,root,root) %{_bindir}/pnewarea
%attr(755,root,root) %{_bindir}/pnewgrp
%attr(755,root,root) %{_bindir}/ptest
%attr(755,root,root) %{_bindir}/ptrans

%attr(755,root,root) %{_bindir}/p_areas
%attr(755,root,root) %{_bindir}/p_con
%attr(755,root,root) %{_bindir}/p_groups
%attr(755,root,root) %{_bindir}/p_gtog
%attr(755,root,root) %{_bindir}/p_loc
%attr(755,root,root) %{_bindir}/p_maint
%attr(755,root,root) %{_bindir}/p_size
%attr(755,root,root) %{_bindir}/pngcrush.stub
%attr(755,root,root) %{_bindir}/pv_desc
%attr(755,root,root) %{_bindir}/pv_last
%attr(755,root,root) %{_bindir}/pv_name
%attr(755,root,root) %{_bindir}/pv_since
%attr(755,root,root) %{_bindir}/pv_sql
%attr(755,root,root) %{_bindir}/rc2sql
%attr(755,root,root) %{_bindir}/viewdeep

%attr(755,root,root) %{_bindir}/bowser

%{_datadir}/pimppa
