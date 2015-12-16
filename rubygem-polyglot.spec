%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name polyglot

Summary:        Allow hooking of language loaders for specified extensions into require
Name:           %{?scl_prefix}rubygem-%{gem_name}
Version:        0.3.3
Release:        4%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://polyglot.rubyforge.org
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       %{?scl_prefix_ruby}ruby(release)
Requires:       %{?scl_prefix_ruby}ruby(rubygems)
Requires:       %{?scl_prefix_ruby}ruby
BuildRequires:  %{?scl_prefix_ruby}ruby(release)
BuildRequires:  %{?scl_prefix_ruby}rubygems-devel
BuildRequires:  %{?scl_prefix_ruby}ruby
BuildArch:      noarch
Provides:       %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This Ruby GEM allows custom language loaders for specified file extensions
to be hooked into require.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}


%prep

%build

%install
%{?scl:scl enable %scl - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/License.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.txt
%{gem_instdir}/Rakefile


%changelog
* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 0.3.3-4
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Thu Jun 20 2013 Josef Stribny <jstribny@redhat.com> - 0.3.3-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.3-2
- Specfile cleanup.

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.3-1
- Rebuilt for scl.
- Updated to 0.3.3.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.3.1-1
- Updated to the latest upstream version.
- Tests enabled.
- Documentation moved into separate package.
- Remove unnecessary Hoe runtime dependency.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-3
- Get rid of duplicate files

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-2
- Bring tests back
- Depend on ruby(abi)
- Replace defines with globals
- Don't delete the world-writable file, fix permissions instead

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.2.5-1
- Package generated by gem2rpm
- Remove log directory
- Don't ship tests
- Fix up License
