#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Tail
Version  : 1.3
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-1.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-1.3.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-tail-perl/libfile-tail-perl_1.3-4.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Tail-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the tail -f directive). Usualy such files are
logfiles of some description.

%package dev
Summary: dev components for the perl-File-Tail package.
Group: Development
Provides: perl-File-Tail-devel = %{version}-%{release}

%description dev
dev components for the perl-File-Tail package.


%package license
Summary: license components for the perl-File-Tail package.
Group: Default

%description license
license components for the perl-File-Tail package.


%prep
%setup -q -n File-Tail-1.3
cd ..
%setup -q -T -D -n File-Tail-1.3 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Tail-1.3/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Tail
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Tail/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/File/Tail.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Tail.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Tail/deblicense_copyright
