#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xmlsec1
Version  : 1.2.24
Release  : 15
URL      : https://github.com/lsh123/xmlsec/archive/xmlsec-1_2_24.tar.gz
Source0  : https://github.com/lsh123/xmlsec/archive/xmlsec-1_2_24.tar.gz
Summary  : XML Security Library implements XML Signature and XML Encryption standards
Group    : Development/Tools
License  : MIT
Requires: xmlsec1-bin
Requires: xmlsec1-lib
Requires: xmlsec1-doc
BuildRequires : gnutls-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : nspr-dev
BuildRequires : nss-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(libxslt)
BuildRequires : pkgconfig(nspr)
BuildRequires : pkgconfig(openssl)
BuildRequires : xz-dev

%description
XMLSec Library
----------------------------------------------
XMLSec library provides C based implementation for major XML Security
standards:

%package bin
Summary: bin components for the xmlsec1 package.
Group: Binaries

%description bin
bin components for the xmlsec1 package.


%package dev
Summary: dev components for the xmlsec1 package.
Group: Development
Requires: xmlsec1-lib
Requires: xmlsec1-bin
Provides: xmlsec1-devel

%description dev
dev components for the xmlsec1 package.


%package doc
Summary: doc components for the xmlsec1 package.
Group: Documentation

%description doc
doc components for the xmlsec1 package.


%package lib
Summary: lib components for the xmlsec1 package.
Group: Libraries

%description lib
lib components for the xmlsec1 package.


%prep
%setup -q -n xmlsec-xmlsec-1_2_24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492695453
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492695453
rm -rf %{buildroot}
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
/usr/include/xmlsec1/xmlsec/private/xslt.h
/usr/include/xmlsec1/xmlsec/soap.h
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
%defattr(-,root,root,-)
%doc /usr/share/doc/xmlsec1/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxmlsec1-gcrypt.so.1
/usr/lib64/libxmlsec1-gcrypt.so.1.2.24
/usr/lib64/libxmlsec1-gnutls.so.1
/usr/lib64/libxmlsec1-gnutls.so.1.2.24
/usr/lib64/libxmlsec1-nss.so.1
/usr/lib64/libxmlsec1-nss.so.1.2.24
/usr/lib64/libxmlsec1-openssl.so.1
/usr/lib64/libxmlsec1-openssl.so.1.2.24
/usr/lib64/libxmlsec1.so.1
/usr/lib64/libxmlsec1.so.1.2.24