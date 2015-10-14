__author__ = 'igorpodobnik'
import random
prestolnice = {
"Alzirija" : "Alzir",
"Angola" : "Luanda",
"Benin" : "Porto Novo, Cotonou",
"Bocvana" : "Gaborone",
"Burundi" : "Bujumbura",
"Burkina Faso" : "Ouagadougou",
"cad" : "N'Djamena",
"Dzibuti" : "Dzibuti (mesto)",
"Egipt" : "Kairo",
"Ekvatorialna Gvineja" : "Malabo",
"Eritreja" : "Asmara",
"Etiopija" : "Adis Abeba",
"Gabon" : "Libreville",
"Gambija" : "Banjul",
"Gana" : "Akra",
"Gvineja" : "Conakry",
"Gvineja Bissau" : "Bissau",
"Juzna Afrika" : "Kaapstad, Pretorija, Bloemfontein",
"Juzni Sudan" : "Juba",
"Kamerun" : "Yaounde",
"Kenija" : "Nairobi",
"Komori" : "Moroni",
"Republika Kongo" : "Brazzaville",
"Demokraticna republika Kongo" : "Kinsasa",
"Lesoto" : "Maseru",
"Liberija" : "Monrovija",
"Libija" : "Tripoli",
"Madagaskar" : "Antananarivo",
"Malavi" : "Lilongwe",
"Mali" : "Bamako",
"Mavretanija" : "Nouakchott",
"Mauritius" : "Port Louis",
"Maroko" : "Rabat",
"Mozambik" : "Maputo",
"Namibija" : "Windhoek",
"Niger" : "Niamey",
"Nigerija" : "Abuja",
"Ruanda" : "Kigali",
"Sao Tome in Principe" : "Sao Tome",
"Senegal" : "Dakar",
"Sejseli" : "Viktorija",
"Sierra Leone" : "Freetown",
"Slonokoscena obala" : "Yamoussoukro",
"Somalija" : "Mogadis",
"Srednjeafriska republika" : "Bangui",
"Sudan" : "Kartum",
"Svazi" : "Mbabane",
"Tanzanija" : "Dar es Salaam, Dodoma",
"Togo" : "Lome",
"Tunizija" : "Tunis",
"Uganda" : "Kampala",
"Zahodna Sahara" : "La'youn",
"Zambija" : "Lusaka",
"Zimbabve" : "Harare",
"Afganistan" : "Kabul",
"Armenija" : "Erevan",
"Azerbajdzan" : "Baku",
"Bahrajn" : "Manama",
"Banglades" : "Daka",
"Butan" : "Thimpu",
"Brunej" : "Bandar Seri Begawan",
"Filipini" : "Manila",
"Gruzija" : "Tbilisi",
"Indija" : "New Delhi",
"Indonezija" : "Dzakarta",
"Iran" : "Teheran",
"Irak" : "Bagdad",
"Japonska" : "Tokio",
"Jemen" : "Sana",
"Jordanija" : "Aman",
"Juzna Koreja" : "Seul",
"Kambodza" : "Phnom Penh",
"Katar" : "Doha",
"Kazahstan" : "Astana",
"Kirgizistan" : "Biskek",
"Ljudska republika Kitajska" : "Peking",
"Kuvajt" : "Kuvait City",
"Laos" : "Vientiane",
"Libanon" : "Bejrut",
"Malezija" : "Kuala Lumpur",
"Maldivi" : "Male",
"Mongolija" : "Ulan Bator",
"Mjanmar" : "Yangon",
"Nepal" : "Katmandu",
"Oman" : "Muskat",
"Pakistan" : "Islamabad",
"Saudova Arabija" : "Rijad",
"Singapur" : "Singapur",
"Severna Koreja" : "Pjongjang",
"Sirija" : "Damask",
"srilanka" : "Colombo, Sri Jayawardenepura Kotte",
"Tadzikistan" : "Dusanbej",
"Tajska" : "Bangkok",
"Tajvan" : "Tajpej",
"Turkmenistan" : "Ashabat",
"Zdruzeni arabski emirati" : "Abu Dabi",
"Uzbekistan" : "Taskent",
"Vietnam" : "Hanoj",
"Vzhodni Timor" : "Dili",
"Albanija" : "Tirana",
"Andora" : "Andora la Vella",
"Avstrija" : "Dunaj",
"Belorusija" : "Minsk",
"Belgija" : "Bruselj",
"Bosna in Hercegovina" : "Sarajevo",
"Bolgarija" : "Sofija",
"Hrvaska" : "Zagreb",
"Ciper" : "Nikozija",
"ceska" : "Praga",
"crna gora" : "Podgorica",
"Danska" : "Kobenhavn",
"Estonija" : "Talin",
"Finska" : "Helsinki",
"Francija" : "Pariz",
"Nemcija" : "Berlin",
"Grcija" : "Atene",
"Madzarska" : "Budimpesta",
"Islandija" : "Reykjavik",
"Irska" : "Dublin",
"Italija" : "Rim",
"Latvija" : "Riga",
"Lihtenstajn" : "Vaduz",
"Litva" : "Vilna",
"Luksemburg" : "Luxembourg",
"Makedonija": "Skopje",
"Malta" : "Valeta",
"Moldavija" : "Kisinjev",
"Monako" : "Monako",
"Nizozemska" : "Amsterdam (glavno mesto), Haag (sedez vlade)",
"Norveska" : "Oslo",
"Poljska" : "Varsava",
"Portugalska" : "Lizbona",
"Romunija":"Bukaresta",
"Rusija" : "Moskva",
"San Marino" : "San Marino",
"Srbija" : "Beograd",
"Slovaska" : "Bratislava",
"Slovenija" : "Ljubljana",
"spanija" : "Madrid",
"svedska" : "Stockholm",
"svica" : "Bern",
"Turcija" : "Ankara",
"Ukrajina" : "Kijev",
"Zdruzeno kraljestvo" : "London",
"Vatikan" : "Vatikan",
"Argentina" : "Buenos Aires",
"Bolivija" : "La Paz, Sucre",
"Brazilija" : "Brasilia",
"cile" : "Santiago",
"Ekvador" : "Quito",
"Francoska Gvajana" : "Cayenne (del Francije)",
"Gvajana" : "Georgetown",
"Kolumbija" : "Bogota",
"Paragvaj" : "Asuncion",
"Peru" : "Lima",
"Surinam" : "Paramaribo",
"Urugvaj" : "Montevideo",
"Venezuela" : "Caracas",
"Avstralija" : "Canberra",
"Mikronezija" : "Palikir",
"Fidzi" : "Suva",
"Kiribati" : "Tarawa",
"Marshallovi otoki" : "Majuro",
"Nauru" : "nima",
"Nova Zelandija" : "Wellington",
"Palau" : "Koror",
"Papua Nova Gvineja" : "Port Moresby",
"Samoa" : "Apia",
"Salomonovi otoki" : "Honiara",
"Tonga" : "Nuku'alofa",
"Tuvalu" : "Funafuti",
"Vanuatu" : "Port Vila",
"Antigva in Barbuda" : "St. Johns",
"Bahami" : "Nasav",
"Barbados" : "Bridgetown",
"Belize" : "Belmopan",
"Dominika" : "Rozo",
"Dominikanska republika" : "Santo Domingo",
"Salvador" : "San Salvador",
"Grenada" : "St. Georges",
"Gvatemala" : "Ciudad Guatemala",
"Haiti" : "Port-au-Prince",
"Honduras" : "Tegucigalpa",
"Jamajka" : "Kingston",
"Kanada" : "Ottawa",
"Kostarika" : "San Jose",
"Kuba" : "Havana",
"Mehika" : "Ciudad de Mexico",
"Nikaragva" : "Managva",
"Panama" : "Ciudad de Panama",
"Portoriko" : "San Juan",
"Saint Kitts in Nevis" : "Basseterre",
"Saint Lucia" : "Castries",
"Saint Vincent in Grenadine" : "Kingstown",
"Trinidad in Tobago" : "Port of Spain",
"Zdruzene drzave Amerike" : "Washington DC"
}
random.choice(prestolnice.keys())



#print prestolnice

def par(drzava):
    prestol = prestolnice[drzava]
    return prestol

def main():
    rezultat = 0
    goljuf = 0
    falil = 0

    while 1==1:
        random_key = random.sample(prestolnice, 1)[0]
        #print random_key
        #print prestolnice[random_key]
        vnos = raw_input("Vnesti prestolnico od -- %s --, pazi na velike zacetnice (ce zelis nehati vpisi N): " % random_key)
        if vnos == "N":
            break
        elif vnos == "h":
            goljuf +=1
            print prestolnice[random_key]
            vnos = raw_input("No skopiraj videno za %s, pazi na velike zacetnice: " % random_key)
        elif vnos == prestolnice[random_key]:
            print("Pravilna izbira!")
            rezultat +=1
        else:
            falil +=1
            print ("Nope, napacno! Pravilni odgovor je --- %s ---" % prestolnice[random_key])

    print("Konec igre")
    skup = falil + rezultat + goljuf
    print "Uganili ste " + str(rezultat) + " od " + str(skup) + " iger"





if __name__ == "__main__":
    main()