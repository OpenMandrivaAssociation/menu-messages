%define GTKMDKDATE	20091029
%define MENUDATE  	20100829

Summary:	Localization files for Menu system
Name:		menu-messages
Version:	2011.0
Release:	1
# fwang: see http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/menu-messages/trunk/
# generated by `make tarball`
Source0:	%{name}-%{MENUDATE}.tar.lzma
Source1:	gtk+mdk-%{GTKMDKDATE}.tar.bz2

License:	GPL
Group:		System/Base
Conflicts:	gtk+mdk =< 0.1.6-13mdk
BuildRequires:	gettext
Obsoletes:	mdk-menu-messages < 2008.1
Provides:	mdk-menu-messages = %{version}-%{release}
BuildArch:	noarch

%description
This package includes that translations of the main menu used by the
different desktops and window managers of the distribution;
as well as translations used by specifically added features.

%prep

%setup -q -n %{name} -a 1

%build

%install
mkdir -p %{buildroot}%{_datadir}/locale

#make po_files
for i in ./*.po
do
  langdir="%{buildroot}%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o	${langdir}/menu-messages.mo ${i}
done

# gtk+mdk files
for i in GtkMdkWidgets/*.po
do
  langdir="%{buildroot}%{_datadir}/locale/`basename ${i} .po`/LC_MESSAGES/"
  mkdir -p ${langdir}
  msgfmt -o	${langdir}/gtk+mdk.mo ${i}
done

%find_lang %{name} menu-messages gtk+mdk

%files -f %{name}.lang
%defattr(-,root,root,0755)
