Summary:	Kopete Antispam
Name:		kopete-antispam
Version: 	0.5
Release: 	%mkrel 1 
Source0: 	http://download.sourceforge.net/sourceforge/kopeteantispam/%name-kde4-%version.tar.gz
License: 	GPLv2+
Group: 		Networking/Instant messaging
Url: 		http://kopeteantispam.sourceforge.net
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdenetwork4-devel
Requires:	kopete

%description
Kopete plugin, which allow to ignore spam messages by using simple
answer/question scheme:

Potential spammers receive a simple question, and they are ignored until
they answers question. After they answers correctly, they receive
notification, and your chat window opens. Also, you can skip test for
some contacts, matched by wildcards, specified by configuration dialog.

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_services}/kconfiguredialog/*.desktop
%{_kde_services}/*.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name-kde4-%version

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}


%changelog
* Sun Feb 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.5-1mdv2010.1
+ Revision: 505899
- new release

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 0.4-1mdv2009.1
+ Revision: 319960
- add requires
- update url
- import kopete-antispam


