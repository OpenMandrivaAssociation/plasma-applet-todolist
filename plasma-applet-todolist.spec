%define name	plasma-applet-todolist
%define version	0.4
%define release	3
%define Summary	Todo List plasmoid using akonadi

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/90706-todo_plasmoid-0.4.tar.bz
Patch0:		plasma-applet-todolist-0.4-mdv-fix-category.patch
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://www.kde-look.org/content/show.php/todo+list?content=90706
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
BuildRequires:	akonadi-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:  boost-devel
Requires:	kdepim4-runtime
Provides:   plasma-applet

%description
Plasmoid that shows KOrganizer 'todo' list using akonadi.

%files 
%defattr(-,root,root)
%doc	README COPYING AUTHORS
%{_kde_libdir}/kde4/plasma_engine_todo.so
%{_kde_libdir}/kde4/todoapplet.so
%{_kde_services}/plasma-engine-todo.desktop
%{_kde_services}/todoapplet-default.desktop

#-----------------------------------------------------------------------

%prep
%setup -q -n todo_plasmoid
%patch0 -p0

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
%__rm -rf %{buildroot}


%changelog
* Wed Dec 08 2010 John Balcaen <mikala@mandriva.org> 0.4-2mdv2011.0
+ Revision: 616248
- Fix buildrequires

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 John Balcaen <mikala@mandriva.org> 0.4-1mdv2010.1
+ Revision: 477857
- Update to 0.4
- rename and rediff patch0
- Fix plasmoid category

* Sun Aug 30 2009 John Balcaen <mikala@mandriva.org> 0.3-1mdv2010.0
+ Revision: 422424
- import plasma-applet-todolist

