%define tarname pyFltk

Summary:	Python wrapper for the FLTK library
Name:		python-pyfltk
Version:	1.3.0
Release:	1
License:	GPLv2
Group:		Development/Python
Url:		http://pyfltk.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyfltk/%{tarname}-%{version}.tar.gz
Patch0:		pyFltk-1.3.0rc1-build.patch
Patch1:		pyfltk-1.3.0-linux-3.x-detection.patch
BuildRequires:	swig
BuildRequires:	fltk-devel >= 1.3.0
BuildRequires:	pkgconfig(python)

%description
pyFLTK is a Python wrapper for the Fast Light Tool Kit
cross-platform graphical user-interface library.

%prep
%setup -qn %{tarname}-%{version}
%apply_patches

# (wally) With P0, disable Werror_cflags temporarily to get pkg build
%define Werror_cflags   %nil
sed -i -e 's|@CUSTOM_CFLAGS@|%{optflags}|' setup.py

%build
CPPFLAGS="-DFL_INTERNALS -lGL %{ldflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

rm -rf %{buildroot}%{py_platsitedir}/fltk/docs
rm -rf %{buildroot}%{py_platsitedir}/fltk/test

%files
%doc CHANGES COPYING README TODO
%{py_platsitedir}/fltk/*
%{py_platsitedir}/*info

