# Copyright (c) 2010, Jeremy Cole
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

%define current_version %(grep "VERSION =" system-summary | cut -d'"' -f2)

Name: system-summary
Version: %{current_version}
Release: 0
License: LGPL
URL: http://jcole.us/
Packager: Jeremy Cole <jeremy@jcole.us>
Summary: Provide a concise summary of hardware present in a system.
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: perl-Parse-DMIDecode

%description
Provide a concise summary of hardware present in a system. Mostly works with HP.

%define _builddir .

%prep
mkdir -p %{buildroot}/usr/sbin
install -m 0755 system-summary %{buildroot}/usr/sbin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/sbin/system-summary
