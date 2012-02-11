#
# Conditional build:
%bcond_with	tests		# perform "make test" (requires configured test server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Test
Summary:	Apache::Test - Test.pm wrapper with helpers for testing Apache
Summary(pl.UTF-8):	Apache::Test - wrapper na Test.pm z funkcjami do testowania Apache
Name:		perl-Apache-Test
Version:	1.37
Release:	1
Epoch:		1
License:	Apache Software License 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	179f247fc5c7d11387b9c73ae3fa6f71
URL:		http://search.cpan.org/dist/Apache-Test/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	apache-mod_env
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# mod_perl 2.x deps, but this module is supposed to work with mod_perl 1.x too
%define		_noautoreq	'perl(Apache2::Const)' 'perl(ModPerl::Config)'

%description
Apache::Test is a wrapper around the standard Test.pm with helpers for
testing an Apache server.

%description -l pl.UTF-8
Apache::Test to moduł opakowujący standardowy Test.pm z funkcjami
pomocniczymi do testowania serwera Apache.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}%{?_rc}

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

#mans make conflict with identical mans from perl-mod_perl
rm -rf $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README SUPPORT ToDo
%{perl_vendorlib}/Apache/Test*.pm
