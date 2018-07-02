#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Tail
Version  : 1.3
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-1.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/File-Tail-1.3.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-tail-perl/libfile-tail-perl_1.3-4.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-File-Tail-man

%description
The File::Tail module is designed for reading files which are continously
appended to (the name comes from the tail -f directive). Usualy such files are
logfiles of some description.

%package man
Summary: man components for the perl-File-Tail package.
Group: Default

%description man
man components for the perl-File-Tail package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n File-Tail-1.3
mkdir -p %{_topdir}/BUILD/File-Tail-1.3/deblicense/
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/File/Tail.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/File::Tail.3
