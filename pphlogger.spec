#
Summary:	PPhlogger - WWW statistic system
Summary(pl):	PPhlogger - system statystyk WWW
Name:		pphlogger
Version:	2.2.5
Release:	0.4
License:	GPL v2
Group:		Applications/WWW
Source0:	http://pphlogger.phpee.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	05e11fd5454ce47919ffc6be929540e4
Source1:	%{name}.conf
URL:		http://pphlogger.phpee.com/
Requires:	php-pcre
Requires:	webserver
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		%{_datadir}/%{name}
%define		_confdir	/etc/%{name}

%description
PowerPhlogger is a complete counter hosting tool. It lets you offer
counter service to others from your site. It's built on PHP and requires
a mySQL server. Your members don't need any PHP-support on their webserver.
They just pass the required data through JavaScript to PPhlogger that is
hosted on your server.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}/{actions,admin,css,img,img/flags,img/colorpages,include} \
	$RPM_BUILD_ROOT%{_phpdir}/{lang,libraries,logs,messages,modules,mysql,ttf_fonts,upgrade} \
	$RPM_BUILD_ROOT{%{_confdir},/etc/httpd}

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

mv -f $RPM_BUILD_ROOT%{_phpdir}/config.inc.php $RPM_BUILD_ROOT%{_confdir}
ln -sf %{_confdir}/config.inc.php $RPM_BUILD_ROOT%{_phpdir}/config.inc.php

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	fi
	if [ -f /var/lock/subsys/httpd ]; then
		/usr/sbin/apachectl restart 1>&2
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{CHANGELOG,doc.html,doc_de.html,INSTALL,README,STANDARDS,TODO}
%attr(640,root,http) %config(noreplace) %{_confdir}/config.inc.php
%attr(640,root,http) %config(noreplace) /etc/httpd/%{name}.conf
%attr(755,root,http) %dir %{_phpdir}
%attr(644,root,http) %{_phpdir}/*.inc
%attr(644,root,http) %{_phpdir}/*.ini
%attr(644,root,http) %{_phpdir}/*.php
%attr(644,root,http) %{_phpdir}/robots.txt
%attr(755,root,http) %dir %{_phpdir}/actions
%attr(644,root,http) %{_phpdir}/actions/*.php
%attr(755,root,http) %dir %{_phpdir}/admin
%attr(755,root,http) %dir %{_phpdir}/css
%attr(644,root,http) %{_phpdir}/css/*.css
%attr(644,root,http) %{_phpdir}/css/*.php
%attr(755,root,http) %dir %{_phpdir}/img
%attr(644,root,http) %{_phpdir}/img/*.gif
%attr(755,root,http) %dir %{_phpdir}/img/colorpages
%attr(644,root,http) %{_phpdir}/img/colorpages/*.gif
%attr(755,root,http) %dir %{_phpdir}/img/flags
# There should be some %lang used??:
%attr(644,root,http) %{_phpdir}/img/flags/*.png
%attr(755,root,http) %dir %{_phpdir}/include
%attr(755,root,http) %dir %{_phpdir}/lang
# There should be some %lang used:
%attr(644,root,http) %{_phpdir}/lang/*.php
%attr(755,root,http) %dir %{_phpdir}/libraries
%attr(644,root,http) %{_phpdir}/libraries/*.js
%attr(644,root,http) %{_phpdir}/libraries/*.php
%attr(755,root,http) %dir %{_phpdir}/logs
%attr(755,root,http) %dir %{_phpdir}/messages
# There should be some %lang used:
%attr(644,root,http) %{_phpdir}/messages/*.txt
%attr(755,root,http) %dir %{_phpdir}/modules
%attr(644,root,http) %{_phpdir}/modules/*.php
%attr(755,root,http) %dir %{_phpdir}/mysql
%attr(644,root,http) %{_phpdir}/mysql/*.sql
%attr(755,root,http) %dir %{_phpdir}/ttf_fonts
%attr(644,root,http) %{_phpdir}/ttf_fonts/*.ttf
%attr(755,root,http) %dir %{_phpdir}/upgrade
%attr(644,root,http) %{_phpdir}/upgrade/*.php

%{_phpdir}/admin/*
%{_phpdir}/include/*
