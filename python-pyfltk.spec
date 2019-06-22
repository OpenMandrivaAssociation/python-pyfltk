%define tarname pyFltk

Summary:	Python wrapper for the FLTK library
Name:		python-pyfltk
Version:	1.3.4.1
Release:	1
License:	GPLv2
Group:		Development/Python
Url:		http://pyfltk.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/aa/3e/773bbde7bace2a403777d2a386dac3b291431101fafb5d5b83ebe0e58cc0/pyFltk-1.3.4.1_py3.tar.gz
BuildRequires:	swig
BuildRequires:	fltk-devel >= 1.3.0
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(libjpeg)

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
CPPFLAGS="-DFL_INTERNALS -lGL %{ldflags}" %{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

rm -rf %{buildroot}%{py_platsitedir}/fltk/docs
rm -rf %{buildroot}%{py_platsitedir}/fltk/test

%files
%doc CHANGES COPYING README TODO
%{py_platsitedir}/fltk/*
%{py_platsitedir}/*info

