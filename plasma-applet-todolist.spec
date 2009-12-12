%define name	plasma-applet-todolist
%define version	0.4
%define release	%mkrel 1
%define Summary	Todo List plasmoid using akonadi

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/90706-todo_plasmoid-0.4.tar.bz
Patch0:		plasma-applet-todolist-0.4-mdv-fix-category.patch
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://www.kde-look.org/content/show.php/todo+list?content=90706
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-devel
BuildRequires:	akonadi-devel
BuildRequires:	kdepimlibs4-devel
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
