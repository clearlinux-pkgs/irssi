#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x00CCB587DDBEF0E1 (staff@irssi.org)
#
Name     : irssi
Version  : 1.1.1
Release  : 30
URL      : https://github.com/irssi/irssi/releases/download/1.1.1/irssi-1.1.1.tar.gz
Source0  : https://github.com/irssi/irssi/releases/download/1.1.1/irssi-1.1.1.tar.gz
Source99 : https://github.com/irssi/irssi/releases/download/1.1.1/irssi-1.1.1.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: irssi-bin = %{version}-%{release}
Requires: irssi-data = %{version}-%{release}
Requires: irssi-lib = %{version}-%{release}
Requires: irssi-license = %{version}-%{release}
Requires: irssi-man = %{version}-%{release}
BuildRequires : glib-dev
BuildRequires : glibc-staticdev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(openssl)

%description
# [Irssi](https://irssi.org/)
[![Build Status](https://travis-ci.org/irssi/irssi.svg?branch=master)](https://travis-ci.org/irssi/irssi)

%package bin
Summary: bin components for the irssi package.
Group: Binaries
Requires: irssi-data = %{version}-%{release}
Requires: irssi-license = %{version}-%{release}
Requires: irssi-man = %{version}-%{release}

%description bin
bin components for the irssi package.


%package data
Summary: data components for the irssi package.
Group: Data

%description data
data components for the irssi package.


%package dev
Summary: dev components for the irssi package.
Group: Development
Requires: irssi-lib = %{version}-%{release}
Requires: irssi-bin = %{version}-%{release}
Requires: irssi-data = %{version}-%{release}
Provides: irssi-devel = %{version}-%{release}

%description dev
dev components for the irssi package.


%package doc
Summary: doc components for the irssi package.
Group: Documentation
Requires: irssi-man = %{version}-%{release}

%description doc
doc components for the irssi package.


%package lib
Summary: lib components for the irssi package.
Group: Libraries
Requires: irssi-data = %{version}-%{release}
Requires: irssi-license = %{version}-%{release}

%description lib
lib components for the irssi package.


%package license
Summary: license components for the irssi package.
Group: Default

%description license
license components for the irssi package.


%package man
Summary: man components for the irssi package.
Group: Default

%description man
man components for the irssi package.


%prep
%setup -q -n irssi-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542932069
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --with-perl-lib=vendor
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542932069
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/irssi
cp COPYING %{buildroot}/usr/share/package-licenses/irssi/COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Irssi.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Irssi/Irc.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Irssi/TextUI.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Irssi/UI.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/.packlist
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/Irc/.packlist
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/TextUI/.packlist
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/UI/.packlist

%files bin
%defattr(-,root,root,-)
/usr/bin/irssi

%files data
%defattr(-,root,root,-)
/usr/share/irssi/help/accept
/usr/share/irssi/help/action
/usr/share/irssi/help/admin
/usr/share/irssi/help/alias
/usr/share/irssi/help/away
/usr/share/irssi/help/ban
/usr/share/irssi/help/beep
/usr/share/irssi/help/bind
/usr/share/irssi/help/cat
/usr/share/irssi/help/cd
/usr/share/irssi/help/channel
/usr/share/irssi/help/clear
/usr/share/irssi/help/completion
/usr/share/irssi/help/connect
/usr/share/irssi/help/ctcp
/usr/share/irssi/help/cycle
/usr/share/irssi/help/dcc
/usr/share/irssi/help/dehilight
/usr/share/irssi/help/deop
/usr/share/irssi/help/devoice
/usr/share/irssi/help/die
/usr/share/irssi/help/disconnect
/usr/share/irssi/help/echo
/usr/share/irssi/help/eval
/usr/share/irssi/help/exec
/usr/share/irssi/help/flushbuffer
/usr/share/irssi/help/format
/usr/share/irssi/help/hash
/usr/share/irssi/help/help
/usr/share/irssi/help/hilight
/usr/share/irssi/help/ignore
/usr/share/irssi/help/info
/usr/share/irssi/help/invite
/usr/share/irssi/help/irssiproxy
/usr/share/irssi/help/ison
/usr/share/irssi/help/join
/usr/share/irssi/help/kick
/usr/share/irssi/help/kickban
/usr/share/irssi/help/kill
/usr/share/irssi/help/knock
/usr/share/irssi/help/knockout
/usr/share/irssi/help/lastlog
/usr/share/irssi/help/layout
/usr/share/irssi/help/levels
/usr/share/irssi/help/links
/usr/share/irssi/help/list
/usr/share/irssi/help/load
/usr/share/irssi/help/log
/usr/share/irssi/help/lusers
/usr/share/irssi/help/map
/usr/share/irssi/help/me
/usr/share/irssi/help/mircdcc
/usr/share/irssi/help/mode
/usr/share/irssi/help/motd
/usr/share/irssi/help/msg
/usr/share/irssi/help/names
/usr/share/irssi/help/nctcp
/usr/share/irssi/help/netsplit
/usr/share/irssi/help/network
/usr/share/irssi/help/nick
/usr/share/irssi/help/notice
/usr/share/irssi/help/notify
/usr/share/irssi/help/op
/usr/share/irssi/help/oper
/usr/share/irssi/help/part
/usr/share/irssi/help/ping
/usr/share/irssi/help/query
/usr/share/irssi/help/quit
/usr/share/irssi/help/quote
/usr/share/irssi/help/rawlog
/usr/share/irssi/help/recode
/usr/share/irssi/help/reconnect
/usr/share/irssi/help/rehash
/usr/share/irssi/help/reload
/usr/share/irssi/help/restart
/usr/share/irssi/help/rmreconns
/usr/share/irssi/help/rmrejoins
/usr/share/irssi/help/save
/usr/share/irssi/help/sconnect
/usr/share/irssi/help/script
/usr/share/irssi/help/scrollback
/usr/share/irssi/help/server
/usr/share/irssi/help/servlist
/usr/share/irssi/help/set
/usr/share/irssi/help/silence
/usr/share/irssi/help/squery
/usr/share/irssi/help/squit
/usr/share/irssi/help/stats
/usr/share/irssi/help/statusbar
/usr/share/irssi/help/time
/usr/share/irssi/help/toggle
/usr/share/irssi/help/topic
/usr/share/irssi/help/trace
/usr/share/irssi/help/ts
/usr/share/irssi/help/unalias
/usr/share/irssi/help/unban
/usr/share/irssi/help/unignore
/usr/share/irssi/help/unload
/usr/share/irssi/help/unnotify
/usr/share/irssi/help/unquery
/usr/share/irssi/help/unsilence
/usr/share/irssi/help/upgrade
/usr/share/irssi/help/uptime
/usr/share/irssi/help/userhost
/usr/share/irssi/help/ver
/usr/share/irssi/help/version
/usr/share/irssi/help/voice
/usr/share/irssi/help/wait
/usr/share/irssi/help/wall
/usr/share/irssi/help/wallops
/usr/share/irssi/help/who
/usr/share/irssi/help/whois
/usr/share/irssi/help/whowas
/usr/share/irssi/help/window
/usr/share/irssi/scripts/autoop.pl
/usr/share/irssi/scripts/autorejoin.pl
/usr/share/irssi/scripts/buf.pl
/usr/share/irssi/scripts/command.pl
/usr/share/irssi/scripts/dns.pl
/usr/share/irssi/scripts/kills.pl
/usr/share/irssi/scripts/mail.pl
/usr/share/irssi/scripts/mlock.pl
/usr/share/irssi/scripts/msg-event.pl
/usr/share/irssi/scripts/quitmsg.pl
/usr/share/irssi/scripts/redirect.pl
/usr/share/irssi/scripts/scriptassist.pl
/usr/share/irssi/scripts/usercount.pl
/usr/share/irssi/themes/colorless.theme
/usr/share/irssi/themes/default.theme

%files dev
%defattr(-,root,root,-)
/usr/include/irssi/irssi-config.h
/usr/include/irssi/irssi-version.h
/usr/include/irssi/src/common.h
/usr/include/irssi/src/core/args.h
/usr/include/irssi/src/core/capsicum.h
/usr/include/irssi/src/core/channel-rec.h
/usr/include/irssi/src/core/channel-setup-rec.h
/usr/include/irssi/src/core/channels-setup.h
/usr/include/irssi/src/core/channels.h
/usr/include/irssi/src/core/chat-protocols.h
/usr/include/irssi/src/core/chatnet-rec.h
/usr/include/irssi/src/core/chatnets.h
/usr/include/irssi/src/core/commands.h
/usr/include/irssi/src/core/core.h
/usr/include/irssi/src/core/expandos.h
/usr/include/irssi/src/core/ignore.h
/usr/include/irssi/src/core/iregex.h
/usr/include/irssi/src/core/levels.h
/usr/include/irssi/src/core/line-split.h
/usr/include/irssi/src/core/log.h
/usr/include/irssi/src/core/masks.h
/usr/include/irssi/src/core/misc.h
/usr/include/irssi/src/core/module.h
/usr/include/irssi/src/core/modules-load.h
/usr/include/irssi/src/core/modules.h
/usr/include/irssi/src/core/net-disconnect.h
/usr/include/irssi/src/core/net-nonblock.h
/usr/include/irssi/src/core/net-sendbuffer.h
/usr/include/irssi/src/core/network-openssl.h
/usr/include/irssi/src/core/network.h
/usr/include/irssi/src/core/nick-rec.h
/usr/include/irssi/src/core/nicklist.h
/usr/include/irssi/src/core/nickmatch-cache.h
/usr/include/irssi/src/core/pidwait.h
/usr/include/irssi/src/core/queries.h
/usr/include/irssi/src/core/query-rec.h
/usr/include/irssi/src/core/rawlog.h
/usr/include/irssi/src/core/recode.h
/usr/include/irssi/src/core/server-connect-rec.h
/usr/include/irssi/src/core/server-rec.h
/usr/include/irssi/src/core/server-setup-rec.h
/usr/include/irssi/src/core/servers-reconnect.h
/usr/include/irssi/src/core/servers-setup.h
/usr/include/irssi/src/core/servers.h
/usr/include/irssi/src/core/session.h
/usr/include/irssi/src/core/settings.h
/usr/include/irssi/src/core/signals.h
/usr/include/irssi/src/core/special-vars.h
/usr/include/irssi/src/core/tls.h
/usr/include/irssi/src/core/utf8.h
/usr/include/irssi/src/core/window-item-def.h
/usr/include/irssi/src/core/window-item-rec.h
/usr/include/irssi/src/core/write-buffer.h
/usr/include/irssi/src/fe-common/core/chat-completion.h
/usr/include/irssi/src/fe-common/core/command-history.h
/usr/include/irssi/src/fe-common/core/completion.h
/usr/include/irssi/src/fe-common/core/fe-capsicum.h
/usr/include/irssi/src/fe-common/core/fe-channels.h
/usr/include/irssi/src/fe-common/core/fe-common-core.h
/usr/include/irssi/src/fe-common/core/fe-core-commands.h
/usr/include/irssi/src/fe-common/core/fe-exec.h
/usr/include/irssi/src/fe-common/core/fe-messages.h
/usr/include/irssi/src/fe-common/core/fe-queries.h
/usr/include/irssi/src/fe-common/core/fe-recode.h
/usr/include/irssi/src/fe-common/core/fe-settings.h
/usr/include/irssi/src/fe-common/core/fe-tls.h
/usr/include/irssi/src/fe-common/core/fe-windows.h
/usr/include/irssi/src/fe-common/core/formats.h
/usr/include/irssi/src/fe-common/core/hilight-text.h
/usr/include/irssi/src/fe-common/core/keyboard.h
/usr/include/irssi/src/fe-common/core/module-formats.h
/usr/include/irssi/src/fe-common/core/module.h
/usr/include/irssi/src/fe-common/core/printtext.h
/usr/include/irssi/src/fe-common/core/themes.h
/usr/include/irssi/src/fe-common/core/window-activity.h
/usr/include/irssi/src/fe-common/core/window-items.h
/usr/include/irssi/src/fe-common/core/windows-layout.h
/usr/include/irssi/src/fe-common/irc/dcc/fe-dcc.h
/usr/include/irssi/src/fe-common/irc/dcc/module-formats.h
/usr/include/irssi/src/fe-common/irc/dcc/module.h
/usr/include/irssi/src/fe-common/irc/fe-irc-channels.h
/usr/include/irssi/src/fe-common/irc/fe-irc-server.h
/usr/include/irssi/src/fe-common/irc/module-formats.h
/usr/include/irssi/src/fe-common/irc/module.h
/usr/include/irssi/src/fe-common/irc/notifylist/module-formats.h
/usr/include/irssi/src/fe-common/irc/notifylist/module.h
/usr/include/irssi/src/fe-text/statusbar-item.h
/usr/include/irssi/src/irc/core/bans.h
/usr/include/irssi/src/irc/core/channel-rejoin.h
/usr/include/irssi/src/irc/core/ctcp.h
/usr/include/irssi/src/irc/core/irc-cap.h
/usr/include/irssi/src/irc/core/irc-channels.h
/usr/include/irssi/src/irc/core/irc-chatnets.h
/usr/include/irssi/src/irc/core/irc-commands.h
/usr/include/irssi/src/irc/core/irc-masks.h
/usr/include/irssi/src/irc/core/irc-nicklist.h
/usr/include/irssi/src/irc/core/irc-queries.h
/usr/include/irssi/src/irc/core/irc-servers-setup.h
/usr/include/irssi/src/irc/core/irc-servers.h
/usr/include/irssi/src/irc/core/irc.h
/usr/include/irssi/src/irc/core/mode-lists.h
/usr/include/irssi/src/irc/core/modes.h
/usr/include/irssi/src/irc/core/module.h
/usr/include/irssi/src/irc/core/netsplit.h
/usr/include/irssi/src/irc/core/sasl.h
/usr/include/irssi/src/irc/core/servers-idle.h
/usr/include/irssi/src/irc/core/servers-redirect.h
/usr/include/irssi/src/irc/dcc/dcc-chat.h
/usr/include/irssi/src/irc/dcc/dcc-file-rec.h
/usr/include/irssi/src/irc/dcc/dcc-file.h
/usr/include/irssi/src/irc/dcc/dcc-get.h
/usr/include/irssi/src/irc/dcc/dcc-queue.h
/usr/include/irssi/src/irc/dcc/dcc-rec.h
/usr/include/irssi/src/irc/dcc/dcc-send.h
/usr/include/irssi/src/irc/dcc/dcc-server.h
/usr/include/irssi/src/irc/dcc/dcc.h
/usr/include/irssi/src/irc/dcc/module.h
/usr/include/irssi/src/irc/flood/module.h
/usr/include/irssi/src/irc/notifylist/module.h
/usr/include/irssi/src/irc/notifylist/notify-setup.h
/usr/include/irssi/src/irc/notifylist/notifylist.h
/usr/include/irssi/src/lib-config/iconfig.h
/usr/include/irssi/src/lib-config/module.h

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/irssi/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/Irc/Irc.so
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/Irssi.so
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/TextUI/TextUI.so
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Irssi/UI/UI.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/irssi/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/irssi.1
