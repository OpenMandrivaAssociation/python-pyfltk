%define tarname pyFltk
%define name	python-pyfltk
%define version	1.1.3
%define release %mkrel 1

Summary:	Python wrapper for the FLTK library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
Url:		http://pyfltk.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	swig >= 1.3.30
BuildRequires:	fltk-devel >= 1.1.7
%py_requires -d

%description 
pyFLTK is a Python wrapper for the Fast Light Tool Kit
cross-platform graphical user-interface library.

%prep
%setup -q -n %{tarname}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}
%__mv %{buildroot}%{py_sitedir}/fltk/docs .
%__mv %{buildroot}%{py_sitedir}/fltk/test .

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README TODO docs/ test/
%{py_sitedir}/fltk/*
%{py_sitedir}/*info
