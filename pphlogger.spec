Summary:	PPhlogger - WWW statistic system
Summary(pl):	PPhlogger - system statystyk WWW
Name:		pphlogger
Version:	2.2.5
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://pphlogger.phpee.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	05e11fd5454ce47919ffc6be929540e4
URL:		http://pphlogger.phpbb.com/
Requires:	php-pcre
Requires:	webserver
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		/home/httpd/html/pphlogger

%description
WWW statistic system.

%description -l pl
System statystyk WWW.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}/{actions,admin,css,img,img/flags,img/colorpages,include} \
	$RPM_BUILD_ROOT%{_phpdir}/{lang,libraries,logs,messages,modules,mysql,ttf_fonts,upgrade}

install *.{php,inc,ini,txt}	$RPM_BUILD_ROOT%{_phpdir}
install actions/*.php		$RPM_BUILD_ROOT%{_phpdir}/actions
install admin/*.php		$RPM_BUILD_ROOT%{_phpdir}/admin
install css/*.{css,php}		$RPM_BUILD_ROOT%{_phpdir}/css
install img/*.gif		$RPM_BUILD_ROOT%{_phpdir}/img
install img/flags/*.png		$RPM_BUILD_ROOT%{_phpdir}/img/flags
install img/colorpages/*.gif	$RPM_BUILD_ROOT%{_phpdir}/img/colorpages
install include/*.{php,txt}	$RPM_BUILD_ROOT%{_phpdir}/include
install lang/*.php		$RPM_BUILD_ROOT%{_phpdir}/lang
install libraries/*.{js,php}	$RPM_BUILD_ROOT%{_phpdir}/libraries
install logs/README		$RPM_BUILD_ROOT%{_phpdir}/logs
install messages/*.txt		$RPM_BUILD_ROOT%{_phpdir}/messages
install modules/*.php		$RPM_BUILD_ROOT%{_phpdir}/modules
install mysql/*.sql		$RPM_BUILD_ROOT%{_phpdir}/mysql
install ttf_fonts/*.ttf		$RPM_BUILD_ROOT%{_phpdir}/ttf_fonts
install upgrade/*.php		$RPM_BUILD_ROOT%{_phpdir}/upgrade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGELOG,doc.html,doc_de.html,INSTALL,README,STANDARDS,TODO}
%attr(755,root,http) %dir %{_phpdir}
%attr(640,root,http) %config(noreplace) %{_phpdir}/config.inc.php
%attr(640,root,http) %{_phpdir}/*.inc
%attr(750,root,http) %dir %{_phpdir}/actions
%attr(750,root,http) %dir %{_phpdir}/admin
%attr(750,root,http) %dir %{_phpdir}/css
%attr(750,root,http) %dir %{_phpdir}/img
%attr(750,root,http) %dir %{_phpdir}/img/flags
%attr(750,root,http) %dir %{_phpdir}/img/colorpages
%attr(750,root,http) %dir %{_phpdir}/include
%attr(750,root,http) %dir %{_phpdir}/lang
%attr(750,root,http) %dir %{_phpdir}/libraries
%attr(750,root,http) %dir %{_phpdir}/logs
%attr(750,root,http) %dir %{_phpdir}/messages
%attr(750,root,http) %dir %{_phpdir}/modules
%attr(750,root,http) %dir %{_phpdir}/mysql
%attr(750,root,http) %dir %{_phpdir}/ttf_fonts
%attr(750,root,http) %dir %{_phpdir}/upgrade

%{_phpdir}/admin/*
%{_phpdir}/include/*
