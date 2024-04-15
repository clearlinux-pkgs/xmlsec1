#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v10
# autospec commit: 5905be9
#
Name     : xmlsec1
Version  : 1.3.4
Release  : 41
URL      : https://github.com/lsh123/xmlsec/archive/xmlsec_1_3_4/xmlsec-1.3.4.tar.gz
Source0  : https://github.com/lsh123/xmlsec/archive/xmlsec_1_3_4/xmlsec-1.3.4.tar.gz
Summary  : XML Security Library implements XML Signature and XML Encryption standards
Group    : Development/Tools
License  : MIT
Requires: xmlsec1-bin = %{version}-%{release}
Requires: xmlsec1-lib = %{version}-%{release}
Requires: xmlsec1-license = %{version}-%{release}
Requires: xmlsec1-man = %{version}-%{release}
BuildRequires : file
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-Requires-to-xmlsec1.patch

%description
# XMLSec Library
XMLSec library provides C based implementation for major XML Security
standards:
- [XML Signature Syntax and Processing](https://www.w3.org/TR/xmldsig-core)
- [XML Encryption Syntax and Processing](https://www.w3.org/TR/xmlenc-core/)

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
Requires: libtool-dev

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
%setup -q -n xmlsec-xmlsec_1_3_4
cd %{_builddir}/xmlsec-xmlsec_1_3_4
%patch -P 1 -p1
pushd ..
cp -a xmlsec-xmlsec_1_3_4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713200026
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713200026
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xmlsec1
cp %{_builddir}/xmlsec-xmlsec_1_3_4/Copyright %{buildroot}/usr/share/package-licenses/xmlsec1/f75f047fc74ec748a8b328071a567b28ee1113e3 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/xmlsec1Conf.sh

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xmlsec1
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
/usr/include/xmlsec1/xmlsec/gnutls/keysstore.h
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
/usr/include/xmlsec1/xmlsec/nss/crypto.h
/usr/include/xmlsec1/xmlsec/nss/keysstore.h
/usr/include/xmlsec1/xmlsec/nss/pkikeys.h
/usr/include/xmlsec1/xmlsec/nss/symbols.h
/usr/include/xmlsec1/xmlsec/nss/x509.h
/usr/include/xmlsec1/xmlsec/openssl/app.h
/usr/include/xmlsec1/xmlsec/openssl/crypto.h
/usr/include/xmlsec1/xmlsec/openssl/evp.h
/usr/include/xmlsec1/xmlsec/openssl/keysstore.h
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
/usr/share/doc/xmlsec1/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libxmlsec1-gcrypt.so.1.3.4
/V3/usr/lib64/libxmlsec1-gnutls.so.1.3.4
/V3/usr/lib64/libxmlsec1-nss.so.1.3.4
/V3/usr/lib64/libxmlsec1-openssl.so.1.3.4
/V3/usr/lib64/libxmlsec1.so.1.3.4
/usr/lib64/libxmlsec1-gcrypt.so.1
/usr/lib64/libxmlsec1-gcrypt.so.1.3.4
/usr/lib64/libxmlsec1-gnutls.so.1
/usr/lib64/libxmlsec1-gnutls.so.1.3.4
/usr/lib64/libxmlsec1-nss.so.1
/usr/lib64/libxmlsec1-nss.so.1.3.4
/usr/lib64/libxmlsec1-openssl.so.1
/usr/lib64/libxmlsec1-openssl.so.1.3.4
/usr/lib64/libxmlsec1.so.1
/usr/lib64/libxmlsec1.so.1.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xmlsec1/f75f047fc74ec748a8b328071a567b28ee1113e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xmlsec1-config.1
/usr/share/man/man1/xmlsec1.1
