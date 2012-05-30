# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=10.0.2
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Thunderbird
Summary(pl.UTF-8):	Pakiety językowe dla Thunderbirda
Name:		mozilla-thunderbird-languages
Version:	12.0.1
Release:	0.1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	f2fa291cf3ddc8388ba7992a88c280be
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	2b548908d867e3430748e5292ef079bf
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	5ded5c4c49babe150b97f5f224bc1fb2
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	d23eae80a9aba1234c3911520e2a71ce
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	4172fcb63fc46e62854e7a5e9518838c
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	c07713249aac72a68cf35a030ea0c591
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	5aa8418e42edb8e96cf07ea8d1a87750
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	105562ae59ed77b91b88d599f5ea6a71
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	516e5c07d33c43d0094086bc10b4f89a
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	66b84848662463e65959c3aaa06ae997
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	f159f86752502fafb466cb096233f379
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	dcb5b8dff1a005fea4482e0ed1170ba4
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	e737042f6c65f23e7d0733af3b0cf786
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	6076fc3f6766979510e1b154335294ab
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	8a847b23778457e597f0c0bb63b0c026
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	f5deaa970704c7c08acfe906e8b54809
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	50d4395066fcc74e061359cd60baf6c2
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	78ee9933557846b10000d162dd402480
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	9f87aeacbf13bfdbc048548c163f8b9d
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	850b606689285dba3f37cb26f1d833f5
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	200567a271ee61926bb7dadaff869f5e
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	85b5866502a68d146e144ba11a3c4ac0
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	915c30387cded4c3489022dbb941137d
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	c06ee703daddd15d1167f263d31a3526
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	9b2cb8d5b22c3ebc10a7d9d98184276a
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	b166f5edeae8047394dee54840d91b46
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	673335ade173a65a6a67e3cb41002d2e
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	1a26c6a1e1beabd9619883fad75fa1ef
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	3d3703eaa406ecd126f4f5b3d67418da
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	98f2941f2786dc6ef7df79d284d8631d
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	e678adcee558299e91f58640601325a5
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	cb9628981c34e65cac62c89ea90c3573
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	c5a82a9870f643a03c1231cfed22d90f
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	48785810322928ee81eeeb6d58817964
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	28c11f259ecea1a5ce5146176de6e014
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	34849106e353f06b55b0142f4be8c254
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	ad07a0b729b3ed55b19d3d2540c06013
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	689278409ec870eb3a10e61c07195a90
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	d4ee9a517adbf228abb5edf518f11937
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	77b47fe41f7c5da0e196f8e59e63913d
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	fa3fdd606d7936f982080fceafe254e0
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	3d13f20190940c254bbbbf7ca3407508
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	311775e9f876223536b82dae231079ec
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	4123c12e399ab41365caa1a594316531
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	756172fb0376ae2279e68868f78bf692
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	87becae2ed75a3f34b10db71039c385d
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	302f9f95780295f1fdd15bfffced949a
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	9ffd74da03a31d421a5a0a95a45d39a3
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	cdd405d02ffb3ba70188d6939ce4d832
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	162969cd099cd2af2b9834042af3cb5b
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	9153507bff7e8e8a4126e13229532150
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	cd0671bac86b8a90938f22e4471f41cb
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	bd36669f09412be0874f3d6380dc2f41
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	cb6de4afe2390712153b6e78f647a6fb
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	fc8d8536293cf90dd32b61956cfc23eb
URL:		http://www.mozilla.org/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		thunderbirddir		%{_libdir}/mozilla-thunderbird

%description
Language packs for Thunderbird.

%description -l pl.UTF-8
Pakiety językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ar
Summary:	Arabic resources for Thunderbird
Summary(pl.UTF-8):	Arabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ar
Arabic resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ast
Summary:	Asturian resources for Thunderbird
Summary(pl.UTF-8):	Asturskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ast
Asturian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ast -l pl.UTF-8
Asturskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-be
Summary:	Belarusian resources for Thunderbird
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-be
Belarusian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-bg
Summary:	Bulgarian resources for Thunderbird
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-bg
Bulgarian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-bn
Summary:	Bengali (Bangladesh) resources for Thunderbird
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu)
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-bn
Bengali (Bangladesh) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Thunderbirda (wersja dla Bangladeszu).

%package -n mozilla-thunderbird-lang-br
Summary:	Breton resources for Thunderbird
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-br
Breton resources for Thunderbird.

%description -n mozilla-thunderbird-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ca
Summary:	Catalan resources for Thunderbird
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ca
Catalan resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-cs
Summary:	Czech resources for Thunderbird
Summary(pl.UTF-8):	Czeskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-cs
Czech resources for Thunderbird.

%description -n mozilla-thunderbird-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-da
Summary:	Danish resources for Thunderbird
Summary(pl.UTF-8):	Duńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-da
Danish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-de
Summary:	German resources for Thunderbird
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-de
German resources for Thunderbird.

%description -n mozilla-thunderbird-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-el
Summary:	Greek resources for Thunderbird
Summary(pl.UTF-8):	Greckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-el
Greek resources for Thunderbird.

%description -n mozilla-thunderbird-lang-el -l pl.UTF-8
Greckie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-en_GB
Summary:	English (British) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-en_GB
English (British) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-en_US
Summary:	English (American) resources for Thunderbird
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-en_US
English (American) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-es_AR
Summary:	Spanish (Andorra) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory)
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-es_AR
Spanish (Andorra) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Andory).

%package -n mozilla-thunderbird-lang-es
Summary:	Spanish (Spain) resources for Thunderbird
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii)
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-es
Spanish (Spain) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Thunderbirda (wersja dla Hiszpanii).

%package -n mozilla-thunderbird-lang-et
Summary:	Estonian resources for Thunderbird
Summary(pl.UTF-8):	Estońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-et
Estonian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-eu
Summary:	Basque resources for Thunderbird
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-eu
Basque resources for Thunderbird.

%description -n mozilla-thunderbird-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-fi
Summary:	Finnish resources for Thunderbird
Summary(pl.UTF-8):	Fińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-fi
Finnish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-fr
Summary:	French resources for Thunderbird
Summary(pl.UTF-8):	Francuskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-fr
French resources for Thunderbird.

%description -n mozilla-thunderbird-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-fy
Summary:	Frisian resources for Thunderbird
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-fy
Frisian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ga
Summary:	Irish resources for Thunderbird
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ga
Irish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-gd
Summary:	Gaelic resources for Thunderbird
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-gd
Gaelic resources for Thunderbird.

%description -n mozilla-thunderbird-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-gl
Summary:	Galician resources for Thunderbird
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-gl
Galician resources for Thunderbird.

%description -n mozilla-thunderbird-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-he
Summary:	Hebrew resources for Thunderbird
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-he
Hebrew resources for Thunderbird.

%description -n mozilla-thunderbird-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-hr
Summary:	Croatian resources for Thunderbird
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-hr
Croatian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-hu
Summary:	Hungarian resources for Thunderbird
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-hu
Hungarian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-hy
Summary:	Armenian resources for Thunderbird
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-hy
Armenian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-id
Summary:	Indonesian resources for Thunderbird
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-id
Indonesian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-is
Summary:	Icelandic resources for Thunderbird
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-is
Icelandic resources for Thunderbird.

%description -n mozilla-thunderbird-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-it
Summary:	Italian resources for Thunderbird
Summary(pl.UTF-8):	Włoskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-it
Italian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ja
Summary:	Japanese resources for Thunderbird
Summary(pl.UTF-8):	Japońskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ja
Japanese resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ko
Summary:	Korean resources for Thunderbird
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ko
Korean resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-lt
Summary:	Lithuanian resources for Thunderbird
Summary(pl.UTF-8):	Litewskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-lt
Lithuanian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-nb
Summary:	Norwegian Bokmaal resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-nb
Norwegian Bokmaal resources for Thunderbird.

%description -n mozilla-thunderbird-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-nl
Summary:	Dutch resources for Thunderbird
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-nl
Dutch resources for Thunderbird.

%description -n mozilla-thunderbird-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-nn
Summary:	Norwegian Nynorsk resources for Thunderbird
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-nn
Norwegian Nynorsk resources for Thunderbird.

%description -n mozilla-thunderbird-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-pa
Summary:	Panjabi resources for Thunderbird
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-pa
Panjabi resources for Thunderbird.

%description -n mozilla-thunderbird-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-pl
Summary:	Polish resources for Thunderbird
Summary(pl.UTF-8):	Polskie pliki językowe dla Thunderbirda
Group:		I18n
URL:		http://www.thunderbird.pl/
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}
Obsoletes:	mozilla-thunderbird-lang-pl

%description -n mozilla-thunderbird-lang-pl
Polish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-pt_BR
Portuguese (Brazil) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-pt
Summary:	Portuguese (Portugal) resources for Thunderbird
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii)
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-pt
Portuguese (Portugal) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Thunderbirda (wersja dla Portugalii).

%package -n mozilla-thunderbird-lang-rm
Summary:	Romansh resources for Thunderbird
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-rm
Romansh resources for Thunderbird.

%description -n mozilla-thunderbird-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ro
Summary:	Romanian resources for Thunderbird
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ro
Romanian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ru
Summary:	Russian resources for Thunderbird
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ru
Russian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-si
Summary:	Sinhala resources for Thunderbird
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-si
Sinhala resources for Thunderbird.

%description -n mozilla-thunderbird-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-sk
Summary:	Slovak resources for Thunderbird
Summary(pl.UTF-8):	Słowackie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-sk
Slovak resources for Thunderbird.

%description -n mozilla-thunderbird-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-sl
Summary:	Slovene resources for Thunderbird
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-sl
Slovene resources for Thunderbird.

%description -n mozilla-thunderbird-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-sq
Summary:	Albanian resources for Thunderbird
Summary(pl.UTF-8):	Albańskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-sq
Albanian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-sr
Summary:	Serbian resources for Thunderbird
Summary(pl.UTF-8):	Serbskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-sr
Serbian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-sv
Summary:	Swedish resources for Thunderbird
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-sv
Swedish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-ta_LK
Summary:	Tamil (Sri Lanka) resources for Thunderbird
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki)
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-ta_LK
Tamil (Sri Lanka) resources for Thunderbird.

%description -n mozilla-thunderbird-lang-ta_LK -l pl.UTF-8
Tamilskie pliki językowe dla Thunderbirda (wersja dla Sri Lanki).

%package -n mozilla-thunderbird-lang-tr
Summary:	Turkish resources for Thunderbird
Summary(pl.UTF-8):	Tureckie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-tr
Turkish resources for Thunderbird.

%description -n mozilla-thunderbird-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-uk
Summary:	Ukrainian resources for Thunderbird
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-uk
Ukrainian resources for Thunderbird.

%description -n mozilla-thunderbird-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-vi
Summary:	Vietnamese resources for Thunderbird
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-vi
Vietnamese resources for Thunderbird.

%description -n mozilla-thunderbird-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-zh_CN
Summary:	Simplified Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-zh_CN
Simplified Chinese resources for Thunderbird.

%description -n mozilla-thunderbird-lang-zh_CN -l pl.UTF-8
Chińskie (uproszczone) pliki językowe dla Thunderbirda.

%package -n mozilla-thunderbird-lang-zh_TW
Summary:	Traditional Chinese resources for Thunderbird
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Thunderbirda
Group:		I18n
Requires:	mozilla-thunderbird >= %{version}
Provides:	mozilla-thunderbird-lang-resources = %{version}

%description -n mozilla-thunderbird-lang-zh_TW
Traditional Chinese resources for Thunderbird.

%description -n mozilla-thunderbird-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Thunderbirda.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 54 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{thunderbirddir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{thunderbirddir}/extensions/langpack-$basename@thunderbird.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mozilla-thunderbird-lang-ar
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ar@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ast
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ast@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-be
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-be@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-bg
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-bg@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-bn
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-bn-BD@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-br
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-br@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ca
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ca@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-cs
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-cs@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-da
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-da@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-de
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-de@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-el
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-el@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-en_GB
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-en-GB@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-en_US
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-en-US@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-es_AR
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-es-AR@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-es
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-es-ES@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-et
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-et@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-eu
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-eu@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-fi
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fi@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-fr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fr@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-fy
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-fy-NL@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ga
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ga-IE@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-gd
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-gd@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-gl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-gl@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-he
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-he@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-hr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hr@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-hu
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hu@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-hy
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-hy-AM@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-id
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-id@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-is
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-is@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-it
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-it@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ja
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ja@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ko
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ko@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-lt
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-lt@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-nb
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nb-NO@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-nl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nl@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-nn
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-nn-NO@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-pa
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pa-IN@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-pl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pl@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-pt_BR
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pt-BR@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-pt
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-pt-PT@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-rm
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-rm@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ro
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ro@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ru
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ru@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-si
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-si@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-sk
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sk@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-sl
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sl@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-sq
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sq@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-sr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sr@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-sv
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-sv-SE@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-ta_LK
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-ta-LK@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-tr
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-tr@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-uk
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-uk@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-vi
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-vi@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-zh_CN
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-zh-CN@thunderbird.mozilla.org.xpi

%files -n mozilla-thunderbird-lang-zh_TW
%defattr(644,root,root,755)
%{thunderbirddir}/extensions/langpack-zh-TW@thunderbird.mozilla.org.xpi
