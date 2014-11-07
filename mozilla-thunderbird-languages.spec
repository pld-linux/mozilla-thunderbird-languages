# TODO:
#  - do something with *.rdf file, there is file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=24.8.1
U=http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Thunderbird
Summary(pl.UTF-8):	Pakiety językowe dla Thunderbirda
Name:		mozilla-thunderbird-languages
Version:	24.8.1
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ar.xpi
# Source0-md5:	df3c934aecd4c80561453f2ae9815b12
Source1:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ast.xpi
# Source1-md5:	1e61a24c8542b309da6df6fb2a5805ec
Source2:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/be.xpi
# Source2-md5:	4f9584c1d976d50feb2eb1d101e1b472
Source3:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bg.xpi
# Source3-md5:	52f37dfae62eab37550827119e1201ec
Source4:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source4-md5:	6fb0becc2a951a8e15ed4b682cb6353d
Source5:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/br.xpi
# Source5-md5:	56cefdf32c4ffb4b59a1c8a1db1b1f21
Source6:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ca.xpi
# Source6-md5:	4338f3a0af12b5c8f648676390a48c92
Source7:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/cs.xpi
# Source7-md5:	5766a0fc10c46b4272ba85f07aa42faf
Source8:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/da.xpi
# Source8-md5:	738999e2f61b2c0d01dd42da432fc022
Source9:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/de.xpi
# Source9-md5:	8ac9c28cf9e1b995770e6a7f2d04f7b2
Source10:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/el.xpi
# Source10-md5:	f232fd236069170e962ae27f15e5f1bf
Source11:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source11-md5:	b13e2f7a3fdfe9d4b43ea20ebc13ed14
Source12:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source12-md5:	39e02ab7ba33b95573e350dee825e883
Source13:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source13-md5:	fd2ebd3a6fe63e9fe76b38eaa79d6fba
Source14:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source14-md5:	4067dae949372decfa9ca93c47b89c83
Source15:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/et.xpi
# Source15-md5:	6eebea405c23790b82f6bbeb060522da
Source16:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/eu.xpi
# Source16-md5:	819dc66ad61fe1977dda034d5d46a4c4
Source17:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fi.xpi
# Source17-md5:	cc018959d1af16af142db76db79c7363
Source18:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fr.xpi
# Source18-md5:	8178edd292e5cf17f1b78457c65621ca
Source19:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source19-md5:	3d9dece8033c961ca1091e0e4c51555f
Source20:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source20-md5:	c3218b6f5a9f73a2d0198198891808f8
Source21:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gd.xpi
# Source21-md5:	55444097cfb23ae04de7345417d890bc
Source22:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/gl.xpi
# Source22-md5:	d3561fd1183b4143dd550920083b05dd
Source23:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/he.xpi
# Source23-md5:	feb25f5c2dc2a9ec0b604e284c1bbcc6
Source24:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hr.xpi
# Source24-md5:	9b9bbfcdcd299ee50eaef9d070688e9d
Source25:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hu.xpi
# Source25-md5:	1637bfaaae6937bd5541b52a34b8c2d3
Source26:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source26-md5:	7f340c88c3e25de1d16d77d12600d5a3
Source27:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/id.xpi
# Source27-md5:	5c89b2874a9fa01b464a54b81ed211af
Source28:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/is.xpi
# Source28-md5:	6b9d56d23c94778a88ede6b5c35bc3dc
Source29:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/it.xpi
# Source29-md5:	804a6f713d58b32e5dd12d3174aec7ab
Source30:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ja.xpi
# Source30-md5:	902edb75662129b72df2865cca62a542
Source31:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ko.xpi
# Source31-md5:	e77dae265a4c46793fee9b8b5a6d6ae5
Source32:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/lt.xpi
# Source32-md5:	fb18cc081be1b640d40bb2791830674d
Source33:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source33-md5:	d4c9f37511206e2fbb8c5ff00e48c06d
Source34:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nl.xpi
# Source34-md5:	1059833e2b2c9363c056da97101ae6af
Source35:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source35-md5:	f203b55d47fa80f4074848711e3b7f4d
Source36:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source36-md5:	4a794d3f86328dd0fc742cb4355a7bc5
Source37:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pl.xpi
# Source37-md5:	22e0469c7f309f6472a19b2899969561
Source38:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source38-md5:	7b3fea7a29644c312912018b80540d5a
Source39:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source39-md5:	de4cc6e159d507893a5692e67de50a56
Source40:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/rm.xpi
# Source40-md5:	4c273038782f5642cc548d24b5b423a9
Source41:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ro.xpi
# Source41-md5:	e87c811db8f21bd5550896308509a482
Source42:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ru.xpi
# Source42-md5:	b5fd25f39a903b87e994d54157b25969
Source43:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/si.xpi
# Source43-md5:	04c1c7490a3a3336850136677df0de10
Source44:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sk.xpi
# Source44-md5:	6b1b621884116b229a4d838a81eb9e62
Source45:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sl.xpi
# Source45-md5:	6c072fe24ca707ae089addd1bb0c09d6
Source46:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sq.xpi
# Source46-md5:	17137f2f9514bd21dc34b7635177f003
Source47:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sr.xpi
# Source47-md5:	098752571fd548c72f65ea6890114fb2
Source48:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source48-md5:	102ba39b36063fcb7fcc5e5967f6aeec
Source49:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/ta-LK.xpi
# Source49-md5:	35edea04d25850625e7ffad6111cd990
Source50:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/tr.xpi
# Source50-md5:	2642559dde7e3097510289660bd7cb51
Source51:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/uk.xpi
# Source51-md5:	da60a4000c7de2baf34df59c69e13341
Source52:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/vi.xpi
# Source52-md5:	a3f0e1d4b1e82d335a08a0d811409edc
Source53:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source53-md5:	fb9de4f16703b2cd7176aeb83ca176a6
Source54:	http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source54-md5:	362d4cd4043a794ed8480ac378da1a4b
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
