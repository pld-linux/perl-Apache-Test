#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires test server configured)
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Test
Summary:	Apache::Test - Test.pm wrapper with helpers for testing Apache
Summary(pl):	Apache::Test - wrapper na Test.pm z funkcjami do testowania Apache
Name:		perl-Apache-Test
Version:	1.09
Release:	1
License:	Apache Software License 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	69ed8680ba3759b3396aaa7ee8b92189
URL:		http://httpd.apache.org/test/
BuildRequires:	apache-mod_perl
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Test is a wrapper around the standard Test.pm with helpers
for testing an Apache server.

%description -l pl
Apache::Test to modu³ opakowuj±cy standardowy Test.pm z funkcjami
pomocniczymi do testowania serwera Apache.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
rm .mypacklist # contains list of files - install will try to remove them
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache/Test*.pm
%{_mandir}/man3/*
