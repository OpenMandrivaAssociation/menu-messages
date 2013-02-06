%define GTKMDKDATE	20091029
%define MENUDATE  	20100829

Summary:	Localization files for Menu system
Name:		menu-messages
Version:	2011.0
Release:	4
License:	GPL
Group:		System/Base
# fwang: see http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/menu-messages/trunk/
# generated by `make tarball`
Source0:	%{name}-%{MENUDATE}.tar.lzma
Source1:	gtk+mdk-%{GTKMDKDATE}.tar.bz2
BuildArch:	noarch
BuildRequires:	gettext

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

%find_lang %{name}
%find_lang gtk+mdk

%files -f %{name}.lang,gtk+mdk.lang
