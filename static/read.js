const langCodes = {'Abkhaz': 'abk', 'Acehnese': 'ace', 'Acholi': 'ach', 'Afar': 'aar', 'Afrikaans': 'af', 'Albanian': 'sq', 'Alur': 'alz', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 'Assamese': 'as', 'Avar': 'ava', 'Awadhi': 'awa', 'Aymara': 'ay', 'Azerbaijani': 'az', 'Balinese': 'ban', 'Baluchi': 'bal', 'Bambara': 'bm', 'Baoulé': 'bci', 'Bashkir': 'bak', 'Basque': 'eu', 'Batak': 'bbc', 'Belarusian': 'be', 'Bemba': 'bem', 'Bengali': 'bn', 'Betawi': 'bew', 'Bhojpuri': 'bho', 'Bikol': 'bik', 'Bosnian': 'bs', 'Breton': 'bre', 'Bulgarian': 'bg', 'Buryat': 'bua', 'Cantonese': 'yue', 'Catalan': 'ca', 'Cebuano': 'ceb', 'Chamorro': 'cha', 'Chechen': 'che', 'Chinese': 'zh-tw', 'Chuukese': 'chk', 'Chuvash': 'chv', 'Corsican': 'co', 'Crimean': 'crh', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dari': 'fa-af', 'Dhivehi': 'dv', 'Dinka': 'din', 'Dogri': 'doi', 'Dombe': 'dom', 'Dutch': 'nl', 'Dyula': 'dyu', 'Dzongkha': 'dzo', 'English': 'en', 'Esperanto': 'eo', 'Estonian': 'et', 'Faroese': 'fao', 'Fijian': 'fij', 'Filipino': 'fil', 'Finnish': 'fi', 'Fon': 'fon', 'French': 'fr', 'Frisian': 'fy', 'Friulian': 'fur', 'Fulani': 'ful', 'Ga': 'gaa', 'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Guarani': 'gn', 'Gujarati': 'gu', 'Haitian': 'ht', 'Hakha': 'cnh', 'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hiligaynon': 'hil', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 'Hunsrik': 'hrx', 'Iban': 'iba', 'Icelandic': 'is', 'Igbo': 'ig', 'Ilocano': 'ilo', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Jamaican': 'jam', 'Japanese': 'ja', 'Javanese': 'jw', 'Jingpo': 'kac', 'Kalaallisut': 'kal', 'Kannada': 'kn', 'Kanuri': 'kau', 'Kapampangan': 'pam', 'Kazakh': 'kk', 'Khasi': 'kha', 'Khmer': 'km', 'Kiga': 'cgg', 'Kikongo': 'kik', 'Kinyarwanda': 'rw', 'Kituba': 'ktu', 'Kokborok': 'trp', 'Komi': 'kom', 'Konkani': 'gom', 'Korean': 'ko', 'Krio': 'kri', 'Kurdish': 'ckb', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latgalian': 'ltg', 'Latin': 'la', 'Latvian': 'lv', 'Ligurian': 'lij', 'Limburgish': 'lim', 'Lingala': 'ln', 'Lithuanian': 'lt', 'Lombard': 'lmo', 'Luganda': 'lg', 'Luo': 'luo', 'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Madurese': 'mad', 'Maithili': 'mai', 'Makassar': 'mak', 'Malagasy': 'mg', 'Malay': 'ms-arab', 'Malayalam': 'ml', 'Maltese': 'mt', 'Mam': 'mam', 'Manx': 'glv', 'Maori': 'mi', 'Marathi': 'mr', 'Marshallese': 'mah', 'Marwadi': 'mwr', 'Mauritian': 'mfe', 'Meadow': 'mhr', 'Meiteilon': 'mni-mtei', 'Minang': 'min', 'Mizo': 'lus', 'Mongolian': 'mn', 'Myanmar': 'my', 'Nahuatl': 'nhe', 'Ndau': 'ndc-zw', 'Ndebele': 'nde', 'Nepalbhasa': 'new', 'Nepali': 'ne', 'Norwegian': 'no', 'Nuer': 'nus', 'Nyanja': 'ny', 'Occitan': 'oci', 'Odia': 'or', 'Oromo': 'om', 'Ossetian': 'oss', 'Pangasinan': 'pag', 'Papiamento': 'pap', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa-arab', "Q'eqchi'": 'kek', 'Quechua': 'qu', 'Romani': 'rom', 'Romanian': 'ro', 'Rundi': 'run', 'Russian': 'ru', 'Sami': 'sme', 'Samoan': 'sm', 'Sango': 'sag', 'Sanskrit': 'sa', 'Santali': 'sat', 'Scots': 'gd', 'Sepedi': 'nso', 'Serbian': 'sr', 'Sesotho': 'st', 'Seychellois': 'crs', 'Shan': 'shn', 'Shona': 'sn', 'Sicilian': 'scn', 'Silesian': 'szl', 'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Susu': 'sus', 'Swahili': 'sw', 'Swati': 'ssw', 'Swedish': 'sv', 'Tagalog': 'tl', 'Tahitian': 'tah', 'Tajik': 'tg', 'Tamazight': 'ber', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Tetum': 'tet', 'Thai': 'th', 'Tibetan': 'bod', 'Tigrinya': 'ti', 'Tiv': 'tiv', 'Tok': 'tpi', 'Tongan': 'ton', 'Tsonga': 'ts', 'Tswana': 'tsn', 'Tulu': 'tcy', 'Tumbuka': 'tum', 'Turkish': 'tr', 'Turkmen': 'tk', 'Tuvan': 'tuk', 'Twi': 'ak', 'Udmurt': 'udm', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Venda': 'ven', 'Venetian': 'vec', 'Vietnamese': 'vi', 'Waray': 'war', 'Welsh': 'cy', 'Wolof': 'wol', 'Xhosa': 'xh', 'Yakut': 'sah', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Yucatec': 'yua', 'Zapotec': 'zap', 'Zulu': 'zu'};
const languagesArray = Object.keys(langCodes);

// Function to populate the select dropdown with languages for both forms
function populateLanguages(selectId) {
    const languageSelect = document.getElementById(selectId);
    
    // Clear any existing options (if needed, e.g. for reset)
    languageSelect.innerHTML = '<option value="" disabled selected>Select a language</option>';
    
    // Loop through the array and create option elements dynamically
    languagesArray.forEach(function(language) {
      const option = document.createElement("option");
      option.value = language;
      option.textContent = language;
      languageSelect.appendChild(option);
    });
}

populateLanguages("language-trans");

document.getElementById("translate-btn").addEventListener("click", function(event) {
    event.preventDefault();
    const selectedLanguage = document.getElementById("language-trans").value;

    if (!selectedLanguage) {
        alert("Please select a language.");
        return;
    }

    const langCode = langCodes[selectedLanguage];

    if (!langCode) {
        alert("Language not supported.");
        return;
    }

    // Redirect with selected language as a GET parameter
    window.location.href = `/read?target_lang=${encodeURIComponent(langCode)}`;
});

document.getElementById("backHome").addEventListener("click", function(event) {
    event.preventDefault();  // Prevents the form from being submitted if the button is inside a form
    window.location.href = '/dashboard';  // Redirect to dashboard
});
