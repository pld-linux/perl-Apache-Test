#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test" (requires configured test server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Test
Summary:	Apache::Test - Test.pm wrapper with helpers for testing Apache
Summary(pl):	Apache::Test - wrapper na Test.pm z funkcjami do testowania Apache
Name:		perl-Apache-Test
Version:	1.27
Release:	2
License:	Apache Software License 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a87aa4e388fe9dd3d19c71d3e414caf
URL:		http://httpd.apache.org/test/
%{?with_autodeps:BuildRequires:	apache-mod_perl}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::Test is a wrapper around the standard Test.pm with helpers for
testing an Apache server.

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
rm -f .mypacklist # contains list of files - install will try to remove them
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Bundle/ApacheTest.pm
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Apache/TestConfigData.pm
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Apache/Test/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache/Test*.pm
%{_mandir}/man3/*
