#
# Conditional build:
%bcond_without	sqlite		# without SQLite support
%bcond_with	mysql		# with MySQL support
%bcond_with	postgresql	# with PostgreSQL support
#
Summary:	KDE Recipe Tool
Summary(pl.UTF-8):	Zarządzanie przepisami w KDE
Name:		krecipes
Version:	0.9.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/krecipes/%{name}-%{version}.tar.gz
# Source0-md5:	7414fd5210561801ba04ee3dad6561d9
URL:		http://krecipes.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_postgresql:BuildRequires:	postgresql-devel}
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this projects was to create a KDE Recipe Tool that:
 - Can manage a recipe database with an easy to use interface
 - Allows creation/removal of new ingredients and units
 - Helps with diets, calculating amount of calories, vitamines,
   carbohydrates... per recipe
 - Creates shopping lists, and daily suggestions for a given diet type
 - Is based on MySQL so it could be possible to generate a KSN
 - Should be as flexible as possible to have the possibility to extend
   it in future.

%description -l pl.UTF-8
Celem tego projektu było stworzenie programu KDE do przepisów, który:
 - potrafi zarządzać bazą danych przepisów z łatwym w użyciu
   interfejsem
 - pozwala tworzyć i usuwać nowe składniki i jednostki
 - pomaga przy dietach, obliczaniu ilości kalorii, witamin,
   węglowodanów itp. dla każdego przepisu
 - tworzy listy zakupów i codzienne sugestie dla zadanego rodzaju
   diety
 - jest oparty na MySQL-u, dzięki czmu można generować KSN
 - powinien być elastyczny i mieć możliwość rozszerzania w
   przyszłości.

%prep
%setup -q

%build
%configure \
	--enable-pch \
	--with%{!?with_sqlite:out}-sqlite \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_postgresql:out}-postgresql \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appsdir=%{_desktopdir}/kde \
	k3bsetup2dir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities $RPM_BUILD_ROOT%{_datadir}/applnk/.hidden

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applnk/.hidden/*.desktop
%dir %{_datadir}/apps/krecipes
%{_datadir}/apps/krecipes/data
%{_datadir}/apps/krecipes/icons
%{_datadir}/apps/krecipes/layouts
%{_datadir}/apps/krecipes/pics
%{_datadir}/apps/krecipes/*.rc
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/*/*/mimetypes/*
%{_iconsdir}/*/*/apps/*
