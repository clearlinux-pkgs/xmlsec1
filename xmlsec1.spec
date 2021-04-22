#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlsec1
Version  : 1.2.32
Release  : 30
URL      : https://github.com/lsh123/xmlsec/archive/xmlsec-1_2_32/xmlsec-1.2.32.tar.gz
Source0  : https://github.com/lsh123/xmlsec/archive/xmlsec-1_2_32/xmlsec-1.2.32.tar.gz
Summary  : XML Security Library implements XML Signature and XML Encryption standards
Group    : Development/Tools
License  : MIT
Requires: xmlsec1-bin = %{version}-%{release}
Requires: xmlsec1-lib = %{version}-%{release}
Requires: xmlsec1-license = %{version}-%{release}
Requires: xmlsec1-man = %{version}-%{release}
BuildRequires : gnutls-dev
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libgcrypt-dev
BuildRequires : nspr-dev
BuildRequires : nss-bin
BuildRequires : nss-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(nspr)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(openssl)
Patch1: 0001-Add-Requires-to-xmlsec1.patch

%description
XMLSec Library
----------------------------------------------
XMLSec library provides C based implementation for major XML Security
standards:

%package bin
Summary: bin components for the xmlsec1 package.
Group: Binaries
Requires: xmlsec1-license = %{version}-%{release}

%description bin
bin components for the xmlsec1 package.


%package dev
Summary: dev components for the xmlsec1 package.
Group: Development
Requires: xmlsec1-lib = %{version}-%{release}
Requires: xmlsec1-bin = %{version}-%{release}
Provides: xmlsec1-devel = %{version}-%{release}
Requires: xmlsec1 = %{version}-%{release}

%description dev
dev components for the xmlsec1 package.


%package doc
Summary: doc components for the xmlsec1 package.
Group: Documentation
Requires: xmlsec1-man = %{version}-%{release}

%description doc
doc components for the xmlsec1 package.


%package lib
Summary: lib components for the xmlsec1 package.
Group: Libraries
Requires: xmlsec1-license = %{version}-%{release}

%description lib
lib components for the xmlsec1 package.


%package license
Summary: license components for the xmlsec1 package.
Group: Default

%description license
license components for the xmlsec1 package.


%package man
Summary: man components for the xmlsec1 package.
Group: Default

%description man
man components for the xmlsec1 package.


%prep
%setup -q -n xmlsec-xmlsec-1_2_32
cd %{_builddir}/xmlsec-xmlsec-1_2_32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619107913
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1619107913
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xmlsec1
cp %{_builddir}/xmlsec-xmlsec-1_2_32/Copyright %{buildroot}/usr/share/package-licenses/xmlsec1/f75f047fc74ec748a8b328071a567b28ee1113e3
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/xmlsec1Conf.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/xmlsec1
/usr/bin/xmlsec1-config

%files dev
%defattr(-,root,root,-)
/usr/include/xmlsec1/xmlsec/app.h
/usr/include/xmlsec1/xmlsec/base64.h
/usr/include/xmlsec1/xmlsec/bn.h
/usr/include/xmlsec1/xmlsec/buffer.h
/usr/include/xmlsec1/xmlsec/crypto.h
/usr/include/xmlsec1/xmlsec/dl.h
/usr/include/xmlsec1/xmlsec/errors.h
/usr/include/xmlsec1/xmlsec/exports.h
/usr/include/xmlsec1/xmlsec/gcrypt/app.h
/usr/include/xmlsec1/xmlsec/gcrypt/crypto.h
/usr/include/xmlsec1/xmlsec/gcrypt/symbols.h
/usr/include/xmlsec1/xmlsec/gnutls/app.h
/usr/include/xmlsec1/xmlsec/gnutls/crypto.h
/usr/include/xmlsec1/xmlsec/gnutls/symbols.h
/usr/include/xmlsec1/xmlsec/gnutls/x509.h
/usr/include/xmlsec1/xmlsec/io.h
/usr/include/xmlsec1/xmlsec/keyinfo.h
/usr/include/xmlsec1/xmlsec/keys.h
/usr/include/xmlsec1/xmlsec/keysdata.h
/usr/include/xmlsec1/xmlsec/keysmngr.h
/usr/include/xmlsec1/xmlsec/list.h
/usr/include/xmlsec1/xmlsec/membuf.h
/usr/include/xmlsec1/xmlsec/nodeset.h
/usr/include/xmlsec1/xmlsec/nss/app.h
/usr/include/xmlsec1/xmlsec/nss/bignum.h
/usr/include/xmlsec1/xmlsec/nss/crypto.h
/usr/include/xmlsec1/xmlsec/nss/keysstore.h
/usr/include/xmlsec1/xmlsec/nss/pkikeys.h
/usr/include/xmlsec1/xmlsec/nss/symbols.h
/usr/include/xmlsec1/xmlsec/nss/x509.h
/usr/include/xmlsec1/xmlsec/openssl/app.h
/usr/include/xmlsec1/xmlsec/openssl/bn.h
/usr/include/xmlsec1/xmlsec/openssl/crypto.h
/usr/include/xmlsec1/xmlsec/openssl/evp.h
/usr/include/xmlsec1/xmlsec/openssl/symbols.h
/usr/include/xmlsec1/xmlsec/openssl/x509.h
/usr/include/xmlsec1/xmlsec/parser.h
/usr/include/xmlsec1/xmlsec/private.h
/usr/include/xmlsec1/xmlsec/strings.h
/usr/include/xmlsec1/xmlsec/templates.h
/usr/include/xmlsec1/xmlsec/transforms.h
/usr/include/xmlsec1/xmlsec/version.h
/usr/include/xmlsec1/xmlsec/x509.h
/usr/include/xmlsec1/xmlsec/xmldsig.h
/usr/include/xmlsec1/xmlsec/xmlenc.h
/usr/include/xmlsec1/xmlsec/xmlsec.h
/usr/include/xmlsec1/xmlsec/xmltree.h
/usr/lib64/libxmlsec1-gcrypt.so
/usr/lib64/libxmlsec1-gnutls.so
/usr/lib64/libxmlsec1-nss.so
/usr/lib64/libxmlsec1-openssl.so
/usr/lib64/libxmlsec1.so
/usr/lib64/pkgconfig/xmlsec1-gcrypt.pc
/usr/lib64/pkgconfig/xmlsec1-gnutls.pc
/usr/lib64/pkgconfig/xmlsec1-nss.pc
/usr/lib64/pkgconfig/xmlsec1-openssl.pc
/usr/lib64/pkgconfig/xmlsec1.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xmlsec1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxmlsec1-gcrypt.so.1
/usr/lib64/libxmlsec1-gcrypt.so.1.2.32
/usr/lib64/libxmlsec1-gnutls.so.1
/usr/lib64/libxmlsec1-gnutls.so.1.2.32
/usr/lib64/libxmlsec1-nss.so.1
/usr/lib64/libxmlsec1-nss.so.1.2.32
/usr/lib64/libxmlsec1-openssl.so.1
/usr/lib64/libxmlsec1-openssl.so.1.2.32
/usr/lib64/libxmlsec1.so.1
/usr/lib64/libxmlsec1.so.1.2.32

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlsec1/f75f047fc74ec748a8b328071a567b28ee1113e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xmlsec1-config.1
/usr/share/man/man1/xmlsec1.1
