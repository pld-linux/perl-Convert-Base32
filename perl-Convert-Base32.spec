#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Convert
%define		pnam	Base32
Summary:	Convert::Base32 - Encoding and decoding of base32 strings
Summary(pl.UTF-8):	Convert::Base32 - kodowanie i dekodowanie łańcuchów base32
Name:		perl-Convert-Base32
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d299467525989850e3a16fac0bf6cc38
URL:		https://metacpan.org/dist/Convert-Base32
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides functions to convert string from / to Base32
encoding, specified in RACE internet-draft. The Base32 encoding is
designed to encode non-ASCII characters in DNS-compatible host name
parts.

%description -l pl.UTF-8
Ten moduł udostępnia funkcje konwersji łańcuchów znaków do i z
kodowania Base32, opisanego w dokumencie roboczym RACE. Kodowanie
Base32 służy do zapisu znaków spoza ASCII w częściach nazw hostów
zgodnych z DNS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/Base32.pm
%{_mandir}/man3/Convert::Base32.3pm*
